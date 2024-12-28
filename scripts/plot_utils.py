import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_histogram(df, column, bins=10):
    """Plot a histogram for a numerical column."""
    plt.figure(figsize=(8, 5))
    sns.histplot(df[column].dropna(), bins=bins, kde=True)
    plt.title(f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.show()

def plot_correlation_matrix(df):
    """Plot a correlation matrix for numerical features."""
    # Select numeric columns
    numeric_df = df.select_dtypes(include=["number"]).apply(pd.to_numeric, errors="coerce").dropna(axis=1, how="all")
    if numeric_df.empty:
        raise ValueError("No numeric data available for correlation matrix.")
    
    # Calculate and plot the matrix
    corr_matrix = numeric_df.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm")
    plt.title("Correlation Matrix")
    plt.show()

def plot_boxplot(df, column, by_column, max_categories=10):
    """
    Plot a boxplot of a column grouped by another, limited to a maximum number of categories.
    
    Parameters:
    - df: DataFrame
    - column: The numeric column to plot.
    - by_column: The categorical column to group by.
    - max_categories: Maximum number of unique categories to include in the plot.
    """
    # Select the first `max_categories` unique categories
    unique_categories = df[by_column].dropna().unique()[:max_categories]
    filtered_df = df[df[by_column].isin(unique_categories)]
    
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=filtered_df, x=by_column, y=column)
    plt.title(f"{column} by {by_column} (Top {max_categories} Categories)")
    plt.xlabel(by_column)
    plt.ylabel(column)
    plt.xticks(rotation=45)
    plt.show()
