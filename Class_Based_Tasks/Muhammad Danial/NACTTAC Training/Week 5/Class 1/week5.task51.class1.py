# PDF class alignment: Binary logistic regression
# Topics: Binary classification using logistic regression.
# Original task implementation retained below.

# NAVTTC AI/ML Course — Task 51: Linear regression
# Source/topic: https://stackabuse.com/linear-regression-in-python-with-scikit-learn/

# Task 51 — Linear Regression using scikit-learn
# Install: python -m pip install scikit-learn matplotlib
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

X = np.array([[1], [2], [3], [4], [5], [6]], dtype=float)
y = np.array([2, 4, 5, 4, 5, 7], dtype=float)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42
)
model = LinearRegression().fit(X_train, y_train)
predictions = model.predict(X_test)
print("Slope:", model.coef_[0], "Intercept:", model.intercept_)
print("Predictions:", predictions)
print("MAE:", mean_absolute_error(y_test, predictions))
print("R²:", r2_score(y_test, predictions))
