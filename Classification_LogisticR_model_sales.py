import numpy as np
import pandas as pd
import matplotlib as matlab
import sklearn as sk
from sklearn import linear_model

from sklearn.linear_model import LogisticRegression

sales=pd.read_csv("https://raw.githubusercontent.com/venkatareddykonasani/Datasets/master/Product%20Sales%20Data/Product_sales.csv")

d1=pd.DataFrame({"Age":[4]})
d2=pd.DataFrame({"Age":[105]})

lg = LogisticRegression()
lg.fit(sales[["Age"]], sales["Bought"])

predict_age1 = lg.predict(d1)
print(predict_age1)

predict_age2 = lg.predict(d2)
print(predict_age2)