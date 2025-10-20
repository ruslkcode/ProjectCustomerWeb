"""
Module for processing raw data from users.
"""
import pandas as pd
from sklearn.preprocessing import StandardScaler


def data_manipulation(df: pd.DataFrame) -> pd.DataFrame:
    """
    Process raw data: inspection, transformation and normalization.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input DataFrame with raw data
    
    Returns:
    --------
    pd.DataFrame
        Processed and normalized DataFrame
    """
    # Create a copy to avoid modifying the original DataFrame
    df_processed = df.copy()
    
    # Data Transformation
    # Convert categorical variables to dummy variables
    df_processed = pd.get_dummies(df_processed, drop_first=True)
    
    # Select numeric columns for standardization
    numeric_columns = df_processed.select_dtypes(include=['int64', 'float64']).columns.tolist()
    
    # Standardize numeric columns
    if numeric_columns:
        scaler = StandardScaler()
        df_processed[numeric_columns] = scaler.fit_transform(df_processed[numeric_columns])
    
    return df_processed


def load_sample_data():
    """
    Load sample data for testing.
    
    Returns:
    --------
    pd.DataFrame
        Sample DataFrame
    """
    import openml
    dataset = openml.datasets.get_dataset(46938)
    df, *_ = dataset.get_data()
    return df


# Example usage (runs only when file is executed directly)
if __name__ == "__main__":
    # Load test data
    df = load_sample_data()
    
    print("Original data shape:", df.shape)
    
    # Process the data
    processed_df = data_manipulation(df)
    
    print("Processed data shape:", processed_df.shape)
    print("\nFirst rows of processed data:")
    print(processed_df.head())