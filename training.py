from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import f1_score, roc_auc_score, average_precision_score
import openml
from data_manipulations import data_manipulation
from sklearn.metrics import f1_score, roc_auc_score, accuracy_score
import joblib

dataset = openml.datasets.get_dataset(46938)
df, *_ = dataset.get_data()
data_train = data_manipulation(df)
y = data_train['bad_client_target_Yes']
X = data_train.drop(labels = 'bad_client_target_Yes', axis=1,)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, train_size = 0.8, random_state = 42)

model = KNeighborsClassifier(
    n_neighbors = 5,
    weights= 'distance',
    algorithm = 'auto',
    leaf_size = 30,
    p = 2,
    metric='minkowski',    
)

model_trained = model.fit(X_train, y_train)

prediction = model.predict(X_test)

y_true = y_test
y_score = model.predict_proba(X_test)[:, 1]
roc = roc_auc_score(
    y_true,
    y_score
)
threshold = 0.1
y_pred = (y_score > threshold).astype(int)

f1 = f1_score(
    y_true,
    y_pred

)
accuracy = accuracy_score(y_true, y_pred)
pr_auc = average_precision_score(y_true, y_score)

grid = GridSearchCV(
    estimator=model,
    param_grid={
        'n_neighbors': [3, 6, 7, 8, 9],
        'weights': ['uniform', 'distance'],
        'metric': ['euclidean', 'manhattan']
    },
    scoring={
        'F1': 'f1',
        'ROC_AUC': 'roc_auc'
    },
    refit='ROC_AUC',
    cv=5
)

grid.fit(X_train, y_train)
best_model = grid.best_estimator_

y_true = y_test
y_score = best_model.predict_proba(X_test)[:, 1]
roc = roc_auc_score(
    y_true,
    y_score
)

threshold = 0.25
y_pred = (y_score > threshold).astype(int)

f1 = f1_score(
    y_true,
    y_pred

)
accuracy = accuracy_score(y_true, y_pred)

pr_auc = average_precision_score(y_true, y_score)

print("Best model parameters:", grid.best_params_)
print("Best model ROC AUC:", roc)
print("Best model F1-score:", f1)
print("Best model Accuracy:", accuracy)
print("Best model PR AUC:", pr_auc)

joblib.dump(best_model, "best_knn_model.joblib")