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
#### Question 2: Find and display the sales of each product using a multiline plot. Display the number of units sold per month for each product using multiline plots.
```python
df = pd.read_csv(data_directory)
monthList = df['month_number'].tolist()
faceCremSalesData = df['facecream'].tolist()
faceWashSalesData = df['facewash'].tolist()
toothPasteSalesData = df['toothpaste'].tolist()
bathingsoapSalesData = df['bathingsoap'].tolist()
shampooSalesData = df['shampoo'].tolist()
moisturizerSalesData = df['moisturizer'].tolist()

plt.plot(monthList, faceCremSalesData,   label='Face Cream Sales Data', marker='o', linewidth=3)
plt.plot(monthList, faceWashSalesData,   label='Face Wash Sales Data',  marker='o', linewidth=3)
plt.plot(monthList, toothPasteSalesData, label='ToothPaste Sales Data', marker='o', linewidth=3)
plt.plot(monthList, bathingsoapSalesData, label='Bathing soap Sales Data', marker='o', linewidth=3)
plt.plot(monthList, shampooSalesData, label='Shampoo Sales Data', marker='o', linewidth=3)
plt.plot(monthList, moisturizerSalesData, label='Moisturizer Sales Data', marker='o', linewidth=3)

plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.legend(loc='upper left')
plt.xticks(monthList)
plt.yticks([1000, 2000, 4000, 6000, 8000, 10000, 12000, 15000, 18000])
plt.title('Sales data')
plt.show()

fig3 = go.Figure()
fig3.add_trace(go.Scatter(x=monthList, y=faceCremSalesData, name='Face Cream Sales Data', mode='lines+markers'))
fig3.add_trace(go.Scatter(x=monthList, y=faceWashSalesData, name='Face Wash Sales Data', mode='lines+markers'))
fig3.add_trace(go.Scatter(x=monthList, y=toothPasteSalesData, name='ToothPaste Sales Data', mode='lines+markers'))
fig3.add_trace(go.Scatter(x=monthList, y=bathingsoapSalesData, name='Bathing soap Sales Data', mode='lines+markers'))
fig3.add_trace(go.Scatter(x=monthList, y=shampooSalesData, name='Shampoo Sales Data', mode='lines+marker
```
#### Question 3: Find toothpaste sales data of each month and display it using a scatterplot. Also, insert a grid in the plot.
```python
df = pd.read_csv(data_directory)
monthList = df['month_number'].tolist()
toothPasteSalesData = df['toothpaste'].tolist()
plt.scatter(monthList, toothPasteSalesData, label='Toothpaste Sales data')
plt.xlabel('Month Number')
plt.ylabel('Number of units Sold')
plt.legend(loc='upper left')
plt.title('Toothpaste Sales data')
plt.xticks(monthList)
plt.grid(True, linewidth=1, linestyle="--")
plt.show()

fig4 = go.Figure()
fig4.add_trace(go.Scatter(x=monthList, y=toothPasteSalesData, mode='markers', name='Toothpaste Sales Data'))
fig4.update_layout(title='Toothpaste Sales data', xaxis_title='Month Number', yaxis_title='Number of units Sold')
```
#### Question 4: Find face cream and face wash product sales data and display it using the bar chart. The bar chart should display the number of units sold per month for each product. Add a separate bar for each product in the same chart.
```python
df = pd.read_csv(data_directory)
monthList = df['month_number'].tolist()
faceCremSalesData = df['facecream'].tolist()
faceWashSalesData = df['facewash'].tolist()

plt.bar([a-0.25 for a in monthList], faceCremSalesData, width=0.25, label='Face Cream Sales Data', align='edge')
plt.bar([a+0.25 for a in monthList], faceWashSalesData, width=-0.25, label='Face Wash Sales Data', align='edge')
plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.legend(loc='upper left')
plt.title(' Sales data')

plt.xticks(monthList)
plt.grid(True, linewidth= 1, linestyle="--")
plt.title('Face Wash and Face Cream Sales Data')
plt.show()

fig5 = go.Figure()
fig5.add_trace(go.Bar(x=monthList, y=faceCremSalesData, name='Face Cream Sales Data'))
fig5.add_trace(go.Bar(x=monthList, y=faceWashSalesData, name='Face Wash Sales Data'))
fig5.update_layout(title='Face wash and Face Cream sales Data', xaxis_title='Month Number', yaxis_title='Sales units in number')
```
#### Question 5: Find the sales data of bathing soap of all months and show it using a bar chart.
```python
df = pd.read_csv(data_directory)
monthList = df['month_number'].tolist()
bathingsoapSalesData = df['bathingsoap'].tolist()
plt.bar(monthList, bathingsoapSalesData)
plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.title('Sales data')
plt.xticks(monthList)
plt.grid(True, linewidth=1, linestyle="--")
plt.title('bathing soap sales data')
plt.show()
fig6 = go.Figure()
fig6.add_trace(go.Bar(x=monthList, y=bathingsoapSalesData, name='Bathing Soap sales data'))
fig6.update_layout(title='Bathing soap sales data', xaxis_title='Month Number', yaxis_title='Sales units in number')
```
#### Question 6: Read Bathing soap facewash of all months and display it using the Subplot.
```python
df = pd.read_csv(data_directory)
monthList = df['month_number'].tolist()
bathingsoap = df['bathingsoap'].tolist()
faceWashSalesData = df['facewash'].tolist()

f, axarr = plt.subplots(2, sharex=True)
axarr[0].plot(monthList, bathingsoap, label='Bathing soap Sales Data', color='k', marker='o', linewidth=3)
axarr[0].set_title('Sales data of  a Bathing soap')
axarr[1].plot(monthList, faceWashSalesData, label='Face Wash Sales Data', color='r', marker='o', linewidth=3)
axarr[1].set_title('Sales data of  a Face Wash')

plt.xticks(monthList)
plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.show()

fig9 = make_subplots(rows=2, cols=1, shared_xaxes=True)
fig9.add_trace(go.Scatter(x=monthList, y=bathingsoapSalesData, mode='lines+markers', name='Bathing soap Sales Data'), row=1, col=1)
fig9.add_trace(go.Scatter(x=monthList, y=faceWashSalesData, mode='lines+markers', name='Face Wash Sales Data'), row=2, col=1)
fig9.update_layout(title='Sales data of a Bathing soap and a Face Wash', xaxis_title='Month Number', yaxis_title='Sales units in number')
```
#### Question 7: Find all product sales data and show it using the stack plot.
```python
df = pd.read_csv(data_directory)
monthList = df['month_number'].tolist()

faceCremSalesData = df['facecream'].tolist()
faceWashSalesData = df['facewash'].tolist()
toothPasteSalesData = df['toothpaste'].tolist()
bathingsoapSalesData = df['bathingsoap'].tolist()
shampooSalesData = df['shampoo'].tolist()
moisturizerSalesData = df['moisturizer'].tolist()

plt.plot([],[],color='m', label='Facecream', linewidth=5)
plt.plot([],[],color='c', label='Facewash', linewidth=5)
plt.plot([],[],color='r', label='Toothpaste', linewidth=5)
plt.plot([],[],color='k', label='Bathing soap', linewidth=5)
plt.plot([],[],color='g', label='Shampoo', linewidth=5)
plt.plot([],[],color='y', label='Moisturizer', linewidth=5)

plt.stackplot(monthList, faceCremSalesData, faceWashSalesData, toothPasteSalesData,
              bathingsoapSalesData, shampooSalesData, moisturizerSalesData,
              colors=['m','c','r','k','g','y'])

plt.xlabel('Month Number')
plt.ylabel('Sales unints in Number')
plt.title('Alll product sales data using stack plot')
plt.legend(loc='upper left')
plt.show()

fig10 = go.Figure()
fig10.add_trace(go.Scatter(x=monthList, y=faceCremSalesData, stackgroup='one', fill='tozeroy', name='Face Cream'))
fig10.add_trace(go.Scatter(x=monthList, y=faceWashSalesData, stackgroup='one', fill='tonexty', name='Face Wash'))
fig10.add_trace(go.Scatter(x=monthList, y=toothPasteSalesData, stackgroup='one', fill='tonexty', name='Toothpaste'))
fig10.add_trace(go.Scatter(x=monthList, y=bathingsoapSalesData, stackgroup='one', fill='tonexty', name='Bathing soap'))
fig10.add_trace(go.Scatter(x=monthList, y=shampooSalesData, stackgroup='one', fill='tonexty', name='Shampoo'))
fig10.add_trace(go.Scatter(x=monthList, y=moisturizerSalesData, stackgroup='one', fill='tonexty', name='Moisturizer'))
fig10.update_layout(title='All product sales data using stack plot', xaxis_title='Month Number', yaxis_title='Sales units in Number')

# Create a subplot with all the plots
fig = make_subplots(rows=5, cols=2, subplot_titles=("Company Sales Data of Last Year","Sales Data of each Product", "Toothpaste Sales Data","Face Wash and Face Cream Sales Data","Bathing soap Sales Data","Sales Data of Bathing soap and Face Wash","All Product Sales Data using Stack Plot"),shared_xaxes=False)

# Add each plot to the subplot
#fig2
fig.add_trace(fig2.data[0], row=1, col=1)
#fig3
fig.add_trace(fig3.data[0], row=1, col=2)
fig.add_trace(fig3.data[1], row=1, col=2)
fig.add_trace(fig3.data[2], row=1, col=2)
fig.add_trace(fig3.data[3], row=1, col=2)
fig.add_trace(fig3.data[4], row=1, col=2)
fig.add_trace(fig3.data[5], row=1, col=2)
#fig4
fig.add_trace(fig4.data[0], row=2, col=1)
#fig5
fig.add_trace(fig5.data[0], row=2, col=2)
fig.add_trace(fig5.data[1], row=2, col=2)
#fig6
fig.add_trace(fig6.data[0], row=3, col=1)
#fig9
fig.add_trace(fig9.data[0], row=3, col=2)
fig.add_trace(fig9.data[1], row=3, col=2)
#fig10
fig.add_trace(fig10.data[0], row=4, col=1)
fig.add_trace(fig10.data[1], row=4, col=1)
fig.add_trace(fig10.data[2], row=4, col=1)
fig.add_trace(fig10.data[3], row=4, col=1)
fig.add_trace(fig10.data[4], row=4, col=1)
fig.add_trace(fig10.data[5], row=4, col=1)

# Update the layout of each subplot to include x-axis and y-axis titles
fig.update_xaxes(title_text='Month Number', row=1, col=1)
fig.update_yaxes(title_text='Profit in Dollar', row=1, col=1)

# Update the layout of Question 3 subplot
fig.update_xaxes(title_text='Month Number', row=1, col=2)
fig.update_yaxes(title_text='Sales Units in Number', row=1, col=2)

# Update the layout of Question 4 subplot
fig.update_xaxes(title_text='Month Number', row=2, col=1)
fig.update_yaxes(title_text='Number of Units Sold', row=2, col=1)

# Update the layout of Question 5 subplot
fig.update_xaxes(title_text='Month Number', row=2, col=2)
fig.update_yaxes(title_text='Sales Units in Number', row=2, col=2)

# Update the layout of Question 6 subplot
fig.update_xaxes(title_text='Month Number', row=3, col=1)
fig.update_yaxes(title_text='Sales Units in Number', row=3, col=1)

# Update the layout of Question 9 subplot
fig.update_xaxes(title_text='Month Number', row=3, col=2)
fig.update_yaxes(title_text='Sales Units in Number', row=3, col=2)

# Update the layout of Question 10 subplot
fig.update_xaxes(title_text='Month Number', row=4, col=1)
fig.update_yaxes(title_text='Sales Units in Number', row=4, col=1)

# Update the layout of the subplot
fig.update_layout(height=1000, title_text="Interactive Plotly Visualizations for Company Sales Data")

# Save the combined plot as an HTML file
fig.write_html('combined_plots.html')
```
### Features

* Interative dashboard
* Data analysis tools

### Technologies used

* Python
* Plotly 
* Excel

### Files Used

- company_sales_data.csv
- combined_plots.html (view live demo by downloading raw file)

### Copyright, Authors, Acknowledgements

I would like to thank GMU's data visualization course for giving me the opportunity to learn and develop my python skills.
