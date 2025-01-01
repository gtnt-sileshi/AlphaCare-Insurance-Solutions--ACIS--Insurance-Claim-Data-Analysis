import pandas as pd
from sklearn.model_selection import train_test_split

def load_data(file_path):
    """
    Loads data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded dataset.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file cannot be parsed into a DataFrame.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found at {file_path}. Please check the path.")
    except ValueError:
        raise ValueError(f"Failed to load data from {file_path}. Ensure it is a valid CSV file.")

def preprocess_data(df):
    """
    Cleans and preprocesses the data.

    Args:
        df (pd.DataFrame): The raw dataset.

    Returns:
        pd.DataFrame: Preprocessed dataset.

    Raises:
        ValueError: If the dataset has no data or required columns are missing.
    """
    if df.empty:
        raise ValueError("The dataset is empty. Check your input file.")
    try:
        # Handle missing values by dropping rows
        df = df.dropna()

        # Encode categorical variables
        df = pd.get_dummies(df, drop_first=True)

        return df
    except KeyError as e:
        raise ValueError(f"Missing expected column: {e}")

def split_data(df, target_column, test_size=0.2):
    """
    Splits data into train and test sets.

    Args:
        df (pd.DataFrame): Preprocessed dataset.
        target_column (str): Name of the target column.
        test_size (float): Proportion of test data.

    Returns:
        tuple: X_train, X_test, y_train, y_test.

    Raises:
        KeyError: If the target column is not found in the dataset.
    """
    if target_column not in df.columns:
        raise KeyError(f"Target column '{target_column}' not found in dataset.")
    try:
        X = df.drop(columns=[target_column])
        y = df[target_column]
        return train_test_split(X, y, test_size=test_size, random_state=42)
    except Exception as e:
        raise RuntimeError(f"Error splitting data: {e}")
