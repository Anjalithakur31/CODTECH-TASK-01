import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Step 1: Load the dataset
file_name = 'employee_management.csv'  # Replace with your CSV file path
data = pd.read_csv(file_name)

print("Initial Data Preview:")
print(data.head())

# Step 2: Handle Missing Values
# Assuming missing values are in numeric columns, use mean imputation
imputer = SimpleImputer(strategy='mean')
numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
data[numeric_columns] = imputer.fit_transform(data[numeric_columns])

# Step 3: Encode Categorical Variables
# Using LabelEncoder for encoding categorical data
label_encoder = LabelEncoder()
categorical_columns = data.select_dtypes(include=['object']).columns
for col in categorical_columns:
    data[col] = label_encoder.fit_transform(data[col])

# Step 4: Scale Numeric Features
# Using StandardScaler to normalize numerical data
scaler = StandardScaler()
data[numeric_columns] = scaler.fit_transform(data[numeric_columns])

print("\nPreprocessed Data Preview:")
print(data.head())

# Step 5: Save Processed Data to a New CSV
processed_file_name = 'processed_employee_management.csv'
data.to_csv(processed_file_name, index=False)
print(f"\nProcessed data saved to '{processed_file_name}'")
