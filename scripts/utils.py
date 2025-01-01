import matplotlib.pyplot as plt
import seaborn as sns
import shap

def plot_feature_importance(importances, feature_names, title="Feature Importance"):
    """
    Plots feature importance for tree-based models.

    Args:
        importances (array): Importance values for each feature.
        feature_names (list): List of feature names.
        title (str): Title of the plot.

    Returns:
        None
    """
    try:
        sorted_idx = importances.argsort()
        plt.figure(figsize=(10, 8))
        plt.barh(feature_names[sorted_idx], importances[sorted_idx])
        plt.title(title)
        plt.xlabel("Importance")
        plt.show()
    except Exception as e:
        print(f"Error plotting feature importance: {e}")

def shap_analysis(model, X_test):
    """
    Performs SHAP analysis to interpret model predictions.

    Args:
        model: Trained model.
        X_test (pd.DataFrame): Test data.

    Returns:
        None
    """
    try:
        explainer = shap.Explainer(model, X_test)
        shap_values = explainer(X_test)

        # Summary plot
        shap.summary_plot(shap_values, X_test)
    except Exception as e:
        print(f"Error performing SHAP analysis: {e}")
