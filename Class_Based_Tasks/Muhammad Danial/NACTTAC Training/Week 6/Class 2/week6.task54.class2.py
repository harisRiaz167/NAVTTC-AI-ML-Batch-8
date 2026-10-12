# PDF class alignment: Linguistic processing and text features
# Topics: POS/NER tagging, chunking/chinking, lemmatization, WordNet, Bag of Words, feature selection/extraction and document similarity.
# Original task implementation retained below.

# NAVTTC AI/ML Course — Task 54: Support Vector Machine
# Source/topic: https://stackabuse.com/implementing-svm-and-kernel-svm-with-pythons-scikit-learn/

# Task 54 — SVM and kernel SVM
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.25, random_state=42, stratify=data.target
)
for kernel in ["linear", "rbf"]:
    model = make_pipeline(StandardScaler(), SVC(kernel=kernel))
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    print(f"{kernel} SVM accuracy: {accuracy_score(y_test, pred):.3f}")
