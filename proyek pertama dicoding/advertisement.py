import numpy as np
import pandas as pd
from sklearn import model_selection
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn import tree
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

data = pd.read_csv("/content/advertising.csv")
numerical_features  = ['Daily Time Spent on Site', 'Age', 'Area Income', 'Daily Internet Usage']
categorical_features = ['Ad Topic Line', 'City', 'Male', 'Clicked on Ad']

## Drop Any Outlier Data
Q1 = data.quantile(0.25)
Q3 = data.quantile(0.75)
IQR=Q3-Q1
data=data[~((data<(Q1-1.5*IQR))|(data>(Q3+1.5*IQR))).any(axis=1)]

X = data[["Daily Time Spent on Site", "Age", "Area Income", "Daily Internet Usage"]]
y = data['Clicked on Ad']

## Scalling Dataset
scaling = preprocessing.MinMaxScaler(feature_range=(0, 1))
scaling.fit(X)
data_scaling = scaling.transform(X)
data_scaling

## Splitting Dataset
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.3, random_state=0)

## Logistic Regression
lr = LogisticRegression()
lr.fit(X_train,y_train)

## Naive Bayes
nb = GaussianNB()
nb.fit(X_train, y_train)

## Random Forest
model_rf = RandomForestClassifier(n_estimators=100,
                               random_state=0
                              )
model_rf.fit(X_train, y_train)

## Decission Tree
model_dt = DecisionTreeClassifier(max_depth=10)
model_dt.fit(X_train, y_train)

## Predice Model
predict_lr = lr.predict(X_test) ## Logistic Regression
predict_nb = nb.predict(X_test) ## Naive Bayes
predict_rf = model_rf.predict(X_test) ## Random Forest
predict_dt = model_dt.predict(X_test) ## Decission Tree

## Evaluate Model
predicts = {
    'Logistic Regression\t' : predict_lr,
    'Naive Bayes\t\t' : predict_nb,
    'Random Forest\t\t' : predict_rf,
    'Decission Tree\t\t' : predict_dt
}

print("Nilai Accuracy Setiap Model\n")
for key in predicts:
  acc = accuracy_score(y_test, predicts[key])
  print(f"{key}: {acc}")