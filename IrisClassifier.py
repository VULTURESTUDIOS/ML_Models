# -*- coding: utf-8 -*-
"""DecisionTree.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Ei9Cq9hpSUsld84FnqyfRMazNaCEGOSl
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
# %matplotlib inline

from sklearn.datasets import load_iris

iris = load_iris()

iris

iris.target

import seaborn as sns

df = sns.load_dataset('iris')

df.head()

x = df.iloc[:,:-1]
y = iris.target

## train test split
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.33, random_state = 42)

x_train

from sklearn.tree import DecisionTreeClassifier

#post prunning
model = DecisionTreeClassifier(max_depth=2)

model.fit(x_train, y_train)

## Constructing a Decision Tree
from sklearn import tree
plt.figure(figsize=(15,10))
tree.plot_tree(model, filled = True)

#prediction by the model
y_pred = model.predict(x_test)

y_pred

#to check the accuracy of the model
from sklearn.metrics import accuracy_score,classification_report

score = accuracy_score(y_pred, y_test)
score

print(classification_report(y_pred, y_test))

#pre prunning
parameter = {
    'criterion' : ['gini', 'entropy','log_loss'],
    'splitter' : ['best', 'random'],
    'max_depth' : [1,2,3,4,5],
    'max_features' : ['auto', 'sqrt', 'log2'],

}

from sklearn.model_selection import GridSearchCV

model = DecisionTreeClassifier(max_depth =2)
cv = GridSearchCV(model, param_grid = parameter, cv =5, scoring = 'accuracy')

cv.fit(x_train, y_train)

cv.best_params_

y_pred = cv.predict(x_test)

from sklearn.metrics import accuracy_score, classification_report

score = accuracy_score(y_pred, y_test)

score

print(classification_report(y_pred, y_test))

f1 = float(input("sepal length : "))
f2 = float(input("sepal width : "))
f3 = float(input("petal length : "))
f4 = float(input("petal width : "))

ans = cv.predict([[f1,f2,f3,f4]])
if(ans == 0):
  print("setosa")
elif(ans == 1):
  print("versicolour")
else:
  print("Virginica")

