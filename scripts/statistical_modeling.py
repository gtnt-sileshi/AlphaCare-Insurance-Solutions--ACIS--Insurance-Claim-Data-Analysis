from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, r2_score

def train_linear_regression(X_train, y_train):
    """
    Trains a linear regression model.

    Args:
        X_train (pd.DataFrame): Training features.
        y_train (pd.Series): Training target variable.

    Returns:
        LinearRegression: Trained model.

    Raises:
        RuntimeError: If the training process fails.
    """
    try:
        model = LinearRegression()
        model.fit(X_train, y_train)
        return model
    except Exception as e:
        raise RuntimeError(f"Error training Linear Regression model: {e}")

def train_random_forest(X_train, y_train, n_estimators=100):
    """
    Trains a Random Forest model.

    Args:
        X_train (pd.DataFrame): Training features.
        y_train (pd.Series): Training target variable.
        n_estimators (int): Number of trees in the forest.

    Returns:
        RandomForestRegressor: Trained model.

    Raises:
        RuntimeError: If the training process fails.
    """
    try:
        model = RandomForestRegressor(n_estimators=n_estimators, random_state=42)
        model.fit(X_train, y_train)
        return model
    except Exception as e:
        raise RuntimeError(f"Error training Random Forest model: {e}")

def train_xgboost(X_train, y_train):
    """
    Trains an XGBoost model.

    Args:
        X_train (pd.DataFrame): Training features.
        y_train (pd.Series): Training target variable.

    Returns:
        XGBRegressor: Trained model.

    Raises:
        RuntimeError: If the training process fails.
    """
    try:
        model = XGBRegressor(random_state=42)
        model.fit(X_train, y_train)
        return model
    except Exception as e:
        raise RuntimeError(f"Error training XGBoost model: {e}")

def evaluate_model(model, X_test, y_test):
    """
    Evaluates a model's performance.

    Args:
        model: Trained model.
        X_test (pd.DataFrame): Test features.
        y_test (pd.Series): Test target variable.

    Returns:
        tuple: RMSE and R² score.

    Raises:
        RuntimeError: If the evaluation fails.
    """
    try:
        predictions = model.predict(X_test)
        rmse = mean_squared_error(y_test, predictions, squared=False)
        r2 = r2_score(y_test, predictions)
        return rmse, r2
    except Exception as e:
        raise RuntimeError(f"Error evaluating the model: {e}")
