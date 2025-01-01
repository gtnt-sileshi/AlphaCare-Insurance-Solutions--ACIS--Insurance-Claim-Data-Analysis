from scipy.stats import ttest_ind, chi2_contingency

def perform_t_test(group_a, group_b):
    """
    Performs a t-test between two groups.

    Args:
        group_a (pd.Series): Data for group A.
        group_b (pd.Series): Data for group B.

    Returns:
        tuple: Test statistic and p-value.

    Raises:
        ValueError: If the input data is not valid.
    """
    if len(group_a) == 0 or len(group_b) == 0:
        raise ValueError("One of the groups is empty. Ensure data is properly segmented.")
    try:
        stat, p_value = ttest_ind(group_a, group_b, equal_var=False)
        return stat, p_value
    except Exception as e:
        raise RuntimeError(f"Error performing t-test: {e}")

def perform_chi_squared_test(contingency_table):
    """
    Performs a chi-squared test on a contingency table.

    Args:
        contingency_table (pd.DataFrame): Contingency table for chi-squared test.

    Returns:
        tuple: Chi-squared statistic, p-value, and degrees of freedom.

    Raises:
        ValueError: If the contingency table is invalid.
    """
    if contingency_table.empty:
        raise ValueError("Contingency table is empty. Ensure proper data grouping.")
    try:
        chi2, p_value, dof, _ = chi2_contingency(contingency_table)
        return chi2, p_value, dof
    except Exception as e:
        raise RuntimeError(f"Error performing chi-squared test: {e}")
