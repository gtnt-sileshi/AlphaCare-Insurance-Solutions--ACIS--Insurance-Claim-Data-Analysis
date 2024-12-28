import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    """Load dataset from a text file."""
    return pd.read_csv(file_path, delimiter="|")

def summarize_data(df):
    """Summarize the dataset."""
    print("Dataset Info:")
    print(df.info())
    print("\nDescriptive Statistics:")
    print(df.describe())

def plot_histogram(df, column, bins=10):
    """Plot a histogram for a numerical column."""
    plt.figure(figsize=(8, 5))
    sns.histplot(df[column].dropna(), bins=bins, kde=True)
    plt.title(f"Distribution of {column}")
    plt.show()

def plot_correlation_matrix(df):
    """Plot a correlation matrix for numerical features."""
    # Select numeric columns
    numeric_df = df.select_dtypes(include=["number"])
    
    # Drop columns with all NaN values or non-numeric placeholders
    numeric_df = numeric_df.apply(pd.to_numeric, errors="coerce").dropna(axis=1, how="all")
    
    if numeric_df.empty:
        raise ValueError("No numeric data available for correlation matrix.")
    
    # Calculate correlation matrix
    corr_matrix = numeric_df.corr()
    
    # Plot the matrix
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm")
    plt.title("Correlation Matrix")
    plt.show()

