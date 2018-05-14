from typing import Any, Union

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, date
from sklearn.linear_model import LinearRegression

#import CSV file
from pandas import DataFrame, Series
from pandas.core.generic import NDFrame

data = pd.read_csv('../data/SportyFreddy.csv', delimiter=';')
print(data.head())

data_date_str = data['Date']
data_weight = data['Weight']

#convert date strings from CSV to unix
data_date = []
data_date_pred = []
for dates in data_date_str:
    a = datetime.strptime(dates, '%d.%m.%y')
    data_date.append(a.date())
    data_date_pred.append([a.timestamp()])

#remove NaN-values for linear regression model
nan = np.isnan(data_weight)
data_weight_nonan = []
data_date_pred_nonan = []
for i in range(0, len(nan)):
    if not nan[i]:
        data_weight_nonan.append([data_weight[i]])
        data_date_pred_nonan.append(data_date_pred[i])

#linear regression
model = LinearRegression()
model.fit(data_date_pred_nonan, data_weight_nonan)
predicted = model.predict(data_date_pred)

#plot
plt.plot(data_date, data_weight, 'bo')
plt.plot(data_date, predicted)
plt.xlabel('Date')
plt.ylabel('Weight [kg]')
plt.title('Weight')
plt.show()