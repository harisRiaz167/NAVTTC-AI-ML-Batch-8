# PDF class alignment: Multiclass logistic regression and practice
# Topics: Multiclass classification and coding practice.
# Original task implementation retained below.

# NAVTTC AI/ML Course — Task 52: Logistic regression
# Source/topic: https://www.datacamp.com/community/tutorials/understanding-logistic-regression-python

# Task 52 — Logistic Regression classification
# Demonstration dataset; no external MNIST download required.
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

X, y = load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000))
model.fit(X_train, y_train)
pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, pred))
print(classification_report(y_test, pred))
