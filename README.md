### Date created

March 2023

### Project Title

Python Company Sales Analysis & Visualization

### Description

Objective: 

Import necessary libraries and datasets:

```python

import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots

data_directory = '/Users/brianlim/Desktop/company_sales_data.csv'
```
#### Question 1: Find the total profit of all months and create a line plot to illustrate the company sales 

```python
df = pd.read_csv(data_directory)
profitList = df['total_profit'].tolist()
monthList = df['month_number'].tolist()
plt.plot(monthList, profitList, label='Profit data of last year',
         color='r', marker='o', markerfacecolor='k',
         linestyle='--', linewidth=3)
plt.xlabel('Month Number')
plt.ylabel('Profit in dollar')
plt.legend(loc='lower right')
plt.title('Company Sales data of last year')
plt.xticks(monthList)
plt.yticks([

fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=monthList, y=profitList, mode='lines', name='Month-wise Profit Data of Last Year',
                          line=dict(color='red', width=3, dash='dot')))
fig2.update_layout(title='Company Profit per Month', xaxis_title='Month Number', yaxis_title='Profit in dollar')
```


### Features

* Interative dashboard
* Data analysis tools

### Demo

You can view the live demo [here](https://lb0201.github.io/Company-Sales-Analysis/combined_plots.html) 

### Technologies used

* Python
* Plotly 
* Excel

### Files Used

- company_sales_data.csv


### Copyright, Authors, Acknowledgements

I would like to thank GMU's data visualization course for giving me the opportunity to learn and develop my python skills.
