from typing import Any, Union

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, date
from sklearn.linear_model import LinearRegression

import core.DiagramLabeling as DL

#import CSV file
from pandas import DataFrame, Series
from pandas.core.generic import NDFrame

data = pd.read_csv('../data/SportyFreddy.csv', delimiter=';')
print(data.head())

headers = list(data)
data_date_str = data['Date']
#data_weight = data['Weight']

#convert date strings from CSV to unix
data_date = []
data_date_pred = []
for dates in data_date_str:
    a = datetime.strptime(dates, '%d.%m.%y')
    data_date.append(a.date())
    data_date_pred.append([a.timestamp()])

for header in headers[1:]:

    labeling = DL.DiagramLabeling()
    title, y_label = labeling.get_labels(header)

    data_values = data[header]

    #remove NaN-values for linear regression model
    nan = np.isnan(data_values)
    data_values_nonan = []
    data_date_pred_nonan = []
    for i in range(0, len(nan)):
        if not nan[i]:
            data_values_nonan.append([data_values[i]])
            data_date_pred_nonan.append(data_date_pred[i])

    #linear regression
    model = LinearRegression()
    model.fit(data_date_pred_nonan, data_values_nonan)
    predicted = model.predict(data_date_pred)

    #plot
    plt.plot(data_date, data_values, 'bo', ms=10.0, mfc='xkcd:grey', mec='xkcd:grey')
    plt.plot(data_date, predicted,  linewidth=4.0)
    plt.xlabel('Date', size='x-large')
    plt.ylabel(y_label, size='x-large')
    plt.title(title, size='x-large')
    plt.show()