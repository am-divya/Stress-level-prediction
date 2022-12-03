import pandas as pd 
from sklearn.metrics import accuracy_score 
import os
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
#df = np.loadtxt('stressdataset.csv', delimeter = ',')
import matplotlib.pyplot as plt
df= pd.read_csv("E:\cc\divya\DataSet_Stress1 - Sheet1.csv")
df.head()
from sklearn import tree

clf = tree.DecisionTreeClassifier()

# [height, weight, shoe_size]
X = [[5,3,5,2,3,5,5], [2,2,2,1,1,4,2], [2,3,1,0,0,1,1], [1,2,2,2,2,4,4], [4,3,5,2,1,3,5],
     [5,1,1,1,2,2,4], [1,2,3,2,1,5,3],
     [4,1,4,1,0,4,5], [5,3,2,1,1,5,2], [3,3,2,2,2,5,4], [3,2,3,0,2,5,4], [1,3,0,1,0,4,2],
     [2,2,1,0,0,5,1], [1,1,3,2,0,3,2], [2,2,5,2,0,4,3], [1,3,4,1,2,3,2], [1,2,4,1,2,4,3],
     [3,2,3,0,2,5,4], [3,3,2,1,1,4,3], [4,2,1,2,1,5,4], [3,1,5,2,1,4,3], [2,1,4,2,3,5,4],
     [3,1,3,2,2,4,3], [4,3,4,1,2,3,3], [2,2,2,1,1,5,3], [1,3,4,1,0,1,4], [3,2,3,1,0,2,5],
     [2,2,1,2,3,2,5], [4,2,0,2,2,2,5], [2,2,0,1,1,3,4], [3,2,0,1,2,2,5], [1,3,2,0,3,4,4],
     [3,3,3,0,2,2,3], [2,3,4,0,1,3,3], [4,2,1,2,1,2,2], [5,2,2,0,3,3,2], [5,2,1,0,3,2,1],
     [5,3,2,0,0,5,2]]

Y = ['high', 'low', 'low', 'low', 'high', 'low', 'low', 'high',
     'high', 'high', 'high', 'low', 'low', 'low', 'low', 'low', 'low', 'high', 'low',
     'high', 'high', 'high', 'low', 'high', 'low', 'low', 'low', 'low', 'low', 'low', 'low', 'low',
     'low', 'low', 'low', 'low', 'low', 'low']

clf = clf.fit(X, Y)
x1=int(input("Enter Lackof sleeping(0-5)"))
x2=int(input("Enter Headache(0-3)"))
x3=int(input("Enter Dizziness(0-5)"))
x4=int(input("eneter too much of caffeine(0-2)"))
x5=int(input("Enter Too much of alcohol(0-3)"))
x6=int(input("Enter Lack of thinking(0-5)"))
x7=int(input("Enter Overthinking(0-5)" ))
tree.plot_tree(clf)
#tree.plot_tree(X,Y)
#prediction = clf.predict([[3,3,2,2,2,5,4]])[0]
prediction = clf.predict([[x1,x2,x3,x4,x5,x6,x7]])[0]

print(prediction+"stress")
