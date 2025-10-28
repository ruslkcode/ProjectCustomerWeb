from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import f1_score, roc_auc_score, average_precision_score, accuracy_score
import openml
import joblib
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline


dataset = openml.datasets.get_dataset(46938)
df, *_ = dataset.get_data()

y = df['bad_client_target'].map({'Yes': 1, 'No': 0})
X = df.drop(labels = {'bad_client_target', 'sex', 'phone_operator', 'region', 'family_status', "month"}, axis=1,)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, train_size = 0.8, random_state = 42)

categorical_features = ['education', 'product_type', 'is_client', 'having_children_flg']
numeric_features = [col for col in X.columns if col not in categorical_features]

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
    ]
)

pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', KNeighborsClassifier(
        n_neighbors = 5,
        weights= 'distance',
        algorithm = 'auto',
        leaf_size = 30,
        p = 2,
        metric='minkowski', ))
])



grid = GridSearchCV(
    estimator=pipeline,
    param_grid={
        'classifier__n_neighbors': [3, 6, 7, 8, 9],
        'classifier__weights': ['uniform', 'distance'],
        'classifier__metric': ['euclidean', 'manhattan']
    },
    scoring={
        'F1': 'f1',
        'ROC_AUC': 'roc_auc'
    },
    refit='ROC_AUC',
    cv=5
)

grid.fit(X_train, y_train)
best_pipeline = grid.best_estimator_

y_true = y_test
y_score = best_pipeline.predict_proba(X_test)[:, 1]
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

joblib.dump(best_pipeline, "best_knn_pipeline.joblib")