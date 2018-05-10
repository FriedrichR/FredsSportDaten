import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#import CSV file
data = pd.read_csv('../data/SportyFreddy.csv', delimiter=';')
print(data.head())

date = data['Date']
weight = data['Weight']

#plot
plt.plot(date, weight, date, weight, 'bo')
plt.xlabel('Date')
plt.ylabel('Weight [kg]')
plt.title('Weight')
plt.show()