# PDF class alignment: NLP concepts and text preprocessing
# Topics: Syntax, semantics, pragmatics, discourse, NLP directions, NLTK/SpaCy, noise removal, tokenization, stemming, normalization and regex.
# Original task implementation retained below.

# NAVTTC AI/ML Course — Task 53: Decision tree classification
# Source/topic: https://www.datacamp.com/community/tutorials/decision-tree-classification-python

# Task 53 — Decision Tree classification
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.metrics import accuracy_score, classification_report

data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.25, random_state=42, stratify=data.target
)
model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X_train, y_train)
pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, pred))
print(classification_report(y_test, pred, target_names=data.target_names))
print(export_text(model, feature_names=list(data.feature_names)))
