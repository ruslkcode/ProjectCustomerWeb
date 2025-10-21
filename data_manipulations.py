"""
Module for processing raw data from users.
"""
import pandas as pd
from sklearn.preprocessing import StandardScaler


def data_manipulation(df: pd.DataFrame) -> pd.DataFrame:

    df_processed = df.copy()
    
    # Remove duplicates
    df_processed = df_processed.drop_duplicates()
    
    # Identify numeric columns BEFORE encoding (to exclude dummy variables from scaling)
    numeric_columns_before = df_processed.select_dtypes(
        include=['int64', 'int32', 'int16', 'int8', 'uint64', 'uint32', 'uint16', 'uint8', 'float64', 'float32']
    ).columns.tolist()
    
    # Data Transformation
    # Convert categorical variables to dummy variables
    df_processed = pd.get_dummies(df_processed, drop_first=True)
    
    # Keep only numeric columns that existed before encoding (exclude dummy variables)
    numeric_columns_to_scale = [col for col in numeric_columns_before if col in df_processed.columns]
    
    # Standardize numeric columns
    if numeric_columns_to_scale:
        scaler = StandardScaler()
        df_processed[numeric_columns_to_scale] = scaler.fit_transform(df_processed[numeric_columns_to_scale])
    
    return df_processed



# Example usage (runs only when file is executed directly)
if __name__ == "__main__":
    import openml
    dataset = openml.datasets.get_dataset(46938)
    df, *_ = dataset.get_data()
    print("Original data shape:", df.shape)
    
    # Process the data
    processed_df = data_manipulation(df)
    
    print("Processed data shape:", processed_df.shape)
    print("\nFirst rows of processed data:")
    print(processed_df.head())