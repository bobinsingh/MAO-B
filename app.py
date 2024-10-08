import streamlit as st
import pandas as pd
from PIL import Image
import subprocess
import os
import base64
import pickle

# Molecular descriptor calculator
def desc_calc():
    # Performs the descriptor calculation
    bashCommand = "java -Xms2G -Xmx2G -Djava.awt.headless=true -jar ./PaDEL-Descriptor/PaDEL-Descriptor.jar -removesalt -standardizenitro -fingerprints -descriptortypes ./PaDEL-Descriptor/PubchemFingerprinter.xml -dir ./ -file descriptors_output.csv"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    if error:
        st.error("Error occurred while calculating descriptors!")
    else:
        os.remove('molecule.smi')

# File download link generator
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="prediction.csv">Download Predictions</a>'
    return href

# Model building and prediction
def build_model(input_data):
    try:
        # Load the saved regression model
        load_model = pickle.load(open('monoamine_oxidase_bioactivity_model.pkl', 'rb'))
        
        # Apply model to make predictions
        prediction = load_model.predict(input_data)
        st.header('**Prediction output**')
        
        # Prepare results for output
        prediction_output = pd.Series(prediction, name='pIC50')
        molecule_name = pd.Series(load_data[1], name='molecule_name')
        df = pd.concat([molecule_name, prediction_output], axis=1)
        
        # Display and offer file download
        st.write(df)
        st.markdown(filedownload(df), unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Error in model prediction: {e}")

# Logo image
image = Image.open('logo.png')
st.image(image, use_column_width=True)

# Page title and description
st.markdown("""
# Bioactivity Prediction App (Monoamine Oxidase-B)

This app allows you to predict the bioactivity towards inhibiting the `Monoamine Oxidase-B` enzyme. 
`Monoamine Oxidase-B` is a drug target for various Neurological Disorders like Parkinson's, Alzheimer's, etc.
""")

# Sidebar for file upload
with st.sidebar.header('1. Upload your TXT data'):
    uploaded_file = st.sidebar.file_uploader("Upload your input file", type=['txt'])

if st.sidebar.button('Predict'):
    # Ensure a file has been uploaded
    if uploaded_file is not None:
        try:
            # Read input file (SMILES and names)
            load_data = pd.read_table(uploaded_file, sep='\t', header=None)
            
            # Save the input for descriptor calculation
            load_data.to_csv('molecule.smi', sep='\t', header=False, index=False)
            
            # Display input data
            st.header('**Original input data**')
            st.write(load_data)

            # Calculate molecular descriptors
            with st.spinner("Calculating descriptors..."):
                desc_calc()

            # Read calculated descriptors
            st.header('**Calculated molecular descriptors**')
            desc = pd.read_csv('descriptors_output.csv')
            st.write(desc)
            st.write(f"Shape of calculated descriptors: {desc.shape}")

            # Load list of descriptor columns used in the model
            st.header('**Subset of descriptors from previously built models**')
            Xlist = list(pd.read_csv('descriptor_list.csv').columns)

            # Subset calculated descriptors
            if all(col in desc.columns for col in Xlist):
                desc_subset = desc[Xlist]
                st.write(desc_subset)
                st.write(f"Shape of subset descriptors: {desc_subset.shape}")

                # Predict bioactivity with the model
                build_model(desc_subset)
            else:
                st.error("Error: Some required descriptors are missing from the calculated data.")
        
        except Exception as e:
            st.error(f"Error processing file: {e}")
    else:
        st.error("Please upload a file before predicting.")

else:
    st.info('Upload input data in the sidebar to start!')
