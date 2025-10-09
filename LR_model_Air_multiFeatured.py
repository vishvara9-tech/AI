import numpy as np
import pandas as pd
import matplotlib as matlab
import statsmodels.formula.api as sm

air = pd.read_csv("https://raw.githubusercontent.com/venkatareddykonasani/Datasets/master/AirPassengers/AirPassengers.csv")
air.info()


model = sm.ols(formula = 'Passengers ~ Promotion_Budget+Service_Quality_Score+Service_Quality_Score+Holiday_week+Delayed_Cancelled_flight_ind+Inter_metro_flight_ratio+Bad_Weather_Ind+Technical_issues_ind', data=air)
fitted1 = model.fit()
fitted1.summary()