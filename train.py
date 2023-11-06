import pickle

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split, cross_validate, KFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score


# Data preparation

df = pd.read_csv("Pistachio_Dataset.csv")

df.columns = df.columns.str.lower()
df = df.drop('id', axis=1)

df['class'] = (df['class'] == 'Kirmizi_Pistachio').astype(int)

features = list(df.columns)
features.remove('class')


# Data split

df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=23)

df_full_train = df_full_train.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

y_full_train = df_full_train['class'].values
y_test = df_test['class'].values

X_full_train = df_full_train[features].values
X_test = df_test[features].values


# Cross-validation
print('Performing cross-validation')

n_estimators=50
max_depth=5
min_samples_leaf=5

rf = RandomForestClassifier(n_estimators=n_estimators,
                            max_depth=max_depth,
                            min_samples_leaf=min_samples_leaf,
                            random_state=23,
                            n_jobs=-1)

cv_result = cross_validate(rf, X_full_train, y_full_train, scoring='roc_auc')
scores = cv_result['test_score']
print(f'CV ROC AUC score = {scores.mean():.3f} +- {scores.std():.3f}')


# Training final model
print('Training the final model')

rf.fit(X_full_train, y_full_train)

y_pred = rf.predict_proba(X_test)[:, 1]
test_score = roc_auc_score(y_test, y_pred)
print(f'ROC AUC on test dataset = {test_score}')


# Saving model
print('Saving the model')

output_file = 'model.bin'

with open(output_file, 'wb') as f_out:
    pickle.dump(rf, f_out)

print(f'Model saved to {output_file}')