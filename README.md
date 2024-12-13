# CODTECH-TASK-01

**Name**: Anjali Thakur Rakeshbhai  
**Company**: CODETECH IT Solutions  
**ID**: CT08DS421  
**Domain**: Artificial Intelligence  
**Duration**: December 5th 2024 - January 5th 2025  
**Mentor**: Muzammil Ahmed

## Overview

The provided Python script processes an employee management dataset (`employee_management.csv`) by handling missing values, encoding categorical variables, scaling numerical features, and saving the processed data to a new CSV file (`processed_employee_management.csv`). This process is common in data preprocessing, a critical step before conducting further analysis or machine learning tasks.

## Key Features of the Script

1. **Data Loading**:  
   Loads the dataset from a CSV file into a Pandas DataFrame.

2. **Missing Value Handling**:  
   Uses `SimpleImputer` from `sklearn` to replace missing values in numeric columns with the mean of the respective columns.

3. **Categorical Data Encoding**:  
   Applies `LabelEncoder` to convert categorical text data (like department names or gender) into numerical labels.

4. **Feature Scaling**:  
   Uses `StandardScaler` to standardize numeric features, ensuring that all numeric values have a mean of 0 and a standard deviation of 1, which is essential for many machine learning algorithms.

5. **Data Saving**:  
   After processing, the script saves the modified DataFrame to a new CSV file called `processed_employee_management.csv`.

## Technologies Used

1. **Pandas**:  
   A Python library for data manipulation and analysis, providing data structures like DataFrame to work with structured data.

2. **Scikit-learn**:  
   A machine learning library that provides utilities for data preprocessing:  
   - `SimpleImputer`: Handles missing values.  
   - `LabelEncoder`: Encodes categorical data into numerical format.  
   - `StandardScaler`: Scales features by removing the mean and scaling to unit variance.

3. **CSV**:  
   The data is stored in CSV (Comma Separated Values) format, a common and simple format for data storage and exchange.

4. **OUTPUT**:
   ![image](https://github.com/user-attachments/assets/ea377c56-6af6-4d3d-a28f-15e3859994e4)
