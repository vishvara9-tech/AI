import numpy as np
import pandas as pd
import matplotlib as matlab
import statsmodels.formula.api as sm

air = pd.read_csv("https://raw.githubusercontent.com/venkatareddykonasani/Datasets/master/AirPassengers/AirPassengers.csv")
air.info()


model = sm.ols(formula = 'Passengers ~ Promotion_Budget', data=air)
fitted1 = model.fit()
fitted1.summary()