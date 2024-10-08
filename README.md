# QSAR Model for Monoamine Oxidase B (MAO-B) Inhibitors

This repository contains a **QSAR (Quantitative Structure-Activity Relationship) model** developed to predict the pIC50 value for **Monoamine Oxidase B (MAO-B) inhibitors** using a **Random Forest Regressor**. The model is designed to assist in the identification of potential MAO-B inhibitors, a target relevant to **Parkinson's Disease** and other neurological conditions related to dopamine depletion.

## Project Overview

Monoamine Oxidase B (MAO-B) is an enzyme that breaks down dopamine in the brain. Inhibiting this enzyme helps increase dopamine levels, which is a critical treatment approach for **Parkinson's Disease (PD)**. By predicting the inhibitory activity (pIC50) of chemical compounds on MAO-B, this model helps screen potential drug-like molecules.

The model was built using **bioactivity data** from **ChEMBL** and molecular descriptors calculated via **PaDEL** using **881 PubChem fingerprints**. The machine learning model used is a **Random Forest Regressor**, and the model is deployed using **Streamlit** for user interaction.

## Model Features

- **Algorithm**: Random Forest Regressor
- **Target Variable**: pIC50 value (logarithmic inhibitory concentration of a compound)
- **Input Format**: The model requires two columns as input:
  - **SMILES notation**: Structural representation of the compound.
  - **ChEMBL ID**: Identifier for the bioactive molecule from the ChEMBL database.

## Dataset

The model is trained on bioactivity data extracted from the **ChEMBL database**. Molecular descriptors were calculated using **PaDEL-Descriptor** software, which generated **881 PubChem fingerprints** for each molecule. The model predicts the pIC50 value, which is a common measure used in QSAR studies to quantify the potency of a compound as an inhibitor.

---

## Model Workflow

1. **Data Preprocessing**:
   - The dataset is preprocessed to ensure consistency and handle missing values.
   - The molecular descriptors are calculated for each compound using **PaDEL-Descriptor**, which outputs PubChem fingerprints.

2. **Model Training**:
   - A **Random Forest Regressor** is used for modeling. The model was trained and optimized using cross-validation to predict the pIC50 values.

3. **Deployment**:
   - The model is deployed using **Streamlit**. Users can upload their data (containing SMILES and ChEMBL IDs) to obtain predicted pIC50 values for their compounds.

---

## Literature Background

Monoamine Oxidase B (MAO-B) inhibitors have been explored extensively as therapeutic agents for Parkinson's Disease and related disorders. MAO-B is primarily responsible for the breakdown of dopamine in the brain, and its inhibition can help maintain dopamine levels, alleviating symptoms of Parkinson's. Studies have shown that selective MAO-B inhibitors reduce the oxidative stress caused by dopamine metabolism and help slow down neurodegeneration.

Several QSAR models have been proposed to predict the potency of MAO-B inhibitors based on their molecular structures. In this model, **PubChem fingerprints** are used as molecular descriptors, which provide a comprehensive representation of the chemical features of molecules. **Random Forest** is chosen as it is robust against overfitting and performs well in high-dimensional spaces, making it an ideal choice for QSAR modeling.


## Dependencies

The following libraries are required to run the model:

- `pandas`
- `numpy`
- `scikit-learn`
- `PaDEL-Descriptor`
- `Streamlit`

Install the required libraries using `pip`:

```bash
pip install pandas numpy scikit-learn streamlit
