import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

def load_data('/LINEAR REGRESSION/data/accidents-database-.csv'):
    """
    Loads the dataset from the specified CSV file path.
    
    Parameters:
        filepath (str): The file path to the CSV dataset.
    
    Returns:
        pd.DataFrame: Loaded dataset as a pandas DataFrame.
    """
    try:
        data = pd.read_csv(filepath)
        return data
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None

def handle_missing_values(data):
    """
    Handles missing values by replacing them with the mode for categorical features.
    
    Parameters:
        data (pd.DataFrame): The input DataFrame with potential missing values.
    
    Returns:
        pd.DataFrame: DataFrame with missing values handled.
    """
    data['Educational_level'] = data['Educational_level'].fillna(data['Educational_level'].mode()[0])
    data['Driving_experience'] = data['Driving_experience'].fillna(data['Driving_experience'].mode()[0])
    data['Type_of_vehicle'] = data['Type_of_vehicle'].fillna(data['Type_of_vehicle'].mode()[0])
    
    return data

def encode_categorical_features(categorical_features):
    """
    Encodes categorical features using OneHotEncoder and returns the preprocessor.

    Parameters:
        categorical_features (list): List of categorical feature column names.
    
    Returns:
        ColumnTransformer: Preprocessing pipeline for categorical features.
    """
    preprocessor = ColumnTransformer(
        transformers=[('cat', OneHotEncoder(), categorical_features)],
        remainder='passthrough'
    )
    
    return preprocessor

def map_target_variable(data, target_column):
    """
    Maps target variable 'Accident_severity' to numerical values.

    Parameters:
        data (pd.DataFrame): Input dataset.
        target_column (str): The name of the target column.
    
    Returns:
        pd.DataFrame: Data with the target column mapped to numerical values.
    """
    severity_mapping = {
        'Slight Injury': 1,
        'Serious Injury': 2,
        'Fatal Injury': 3
    }
    
    data[target_column] = data[target_column].map(severity_mapping)
 
    data = data.dropna(subset=[target_column])
    
    return data

def split_data(data, features, target, test_size=0.2, random_state=42):
    """
    Splits the dataset into training and testing sets.

    Parameters:
        data (pd.DataFrame): Input dataset.
        features (list): List of feature column names.
        target (str): Target column name.
        test_size (float): Proportion of the data to include in the test split.
        random_state (int): Seed for random splitting.
    
    Returns:
        tuple: X_train, X_test, y_train, y_test
    """
    X = data[features]
    y = data[target]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    return X_train, X_test, y_train, y_test

