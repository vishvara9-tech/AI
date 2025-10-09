import numpy as np
import pandas as pd
import matplotlib as matlab
import sklearn as sk
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn import model_selection

Fiber = pd.read_csv("https://raw.githubusercontent.com/venkatareddykonasani/Datasets/master/Fiberbits/Fiberbits_v1.csv")

lg = LogisticRegression()
lg.fit(Fiber[['income','months_on_network','Num_complaints','number_plan_changes','relocated','monthly_bill','technical_issues_per_month','Speed_test_result']], Fiber[['active_cust']])

p = lg.predict(Fiber[['income']+ ['months_on_network']+ ['Num_complaints']+ ['number_plan_changes']+ ['relocated']+ ['monthly_bill']+ ['technical_issues_per_month']+ ['Speed_test_result']])

cm = confusion_matrix(Fiber[['active_cust']], p)

tot = sum(sum(cm))

accuracy = ((cm[0,0]+cm[1,1])/tot) * 100
print(accuracy)

train_data, test_data = model_selection.train_test_split(Fiber, test_size = 0.2)

print("train data shape", train_data.shape)
print("test data shape", test_data.shape)