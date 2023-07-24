data_directory = '/Users/brianlim/Desktop/company_sales_data.csv'

'''Exercise 1: Read Total profit of all months and show it using a line plot
Total profit data provided for each month. Generated line plot must include the following properties:
X label name = Month Number
Y label name = Total profit'''
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Exercise 1 - Line Plot (Matplotlib)
df = pd.read_csv(data_directory)
profitList = df['total_profit'].tolist()
monthList = df['month_number'].tolist()

plt.plot(monthList, profitList, label='Month-wise Profit data of last year')
plt.xlabel('Month number')
plt.ylabel('Profit in dollar')
plt.xticks(monthList)
plt.title('Company Profit per Month')
plt.yticks([100000, 200000, 300000, 400000, 500000])
plt.show()

# Create the interactive Plotly plot for Exercise 1
fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=monthList, y=profitList, mode='lines', name='Month-wise Profit data of last year'))
fig1.update_layout(title='Company profit per month', xaxis_title='Month Number', yaxis_title='Profit in dollar')

'''Exercise 2: Get total profit of all months and show line plot with the following Style properties
Generated line plot must include following Style properties:
Line Style dotted and Line-color should be red
Show legend at the lower right location.
X label name = Month Number
Y label name = Sold units number
Add a circle marker.
Line marker color as read
Line width should be 3'''
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
plt.yticks([100000, 200000, 300000, 400000, 500000])
plt.show()

# Create the interactive Plotly plot for Exercise 2
fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=monthList, y=profitList, mode='lines', name='Month-wise Profit data of last year',
                          line=dict(color='red', width=3, dash='dot')))
fig2.update_layout(title='Company Profit per Month', xaxis_title='Month Number', yaxis_title='Profit in dollar')


'''Exercise 3: Read all product sales data and show it  using a multiline plot
Display the number of units sold per month for each product using multiline plots. (i.e., Separate Plotline for each product ).'''
df = pd.read_csv(data_directory)
monthList = df['month_number'].tolist()
faceCremSalesData = df['facecream'].tolist()
faceWashSalesData = df['facewash'].tolist()
toothPasteSalesData = df['toothpaste'].tolist()
bathingsoapSalesData = df['bathingsoap'].tolist()
shampooSalesData = df['shampoo'].tolist()
moisturizerSalesData = df['moisturizer'].tolist()

plt.plot(monthList, faceCremSalesData,   label='Face cream Sales Data', marker='o', linewidth=3)
plt.plot(monthList, faceWashSalesData,   label='Face Wash Sales Data',  marker='o', linewidth=3)
plt.plot(monthList, toothPasteSalesData, label='ToothPaste Sales Data', marker='o', linewidth=3)
plt.plot(monthList, bathingsoapSalesData, label='Bathingsoap Sales Data', marker='o', linewidth=3)
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
fig3.add_trace(go.Scatter(x=monthList, y=faceCremSalesData, name='Face cream Sales Data', mode='lines+markers'))
fig3.add_trace(go.Scatter(x=monthList, y=faceWashSalesData, name='Face Wash Sales Data', mode='lines+markers'))
fig3.add_trace(go.Scatter(x=monthList, y=toothPasteSalesData, name='ToothPaste Sales Data', mode='lines+markers'))
fig3.add_trace(go.Scatter(x=monthList, y=bathingsoapSalesData, name='Bathingsoap Sales Data', mode='lines+markers'))
fig3.add_trace(go.Scatter(x=monthList, y=shampooSalesData, name='Shampoo Sales Data', mode='lines+markers'))
fig3.add_trace(go.Scatter(x=monthList, y=moisturizerSalesData, name='Moisturizer Sales Data', mode='lines+markers'))
fig3.update_layout(title='Sales Data', xaxis_title='Month Number', yaxis_title='Sales Units in Number')


'''Exercise 4: Read toothpaste sales data of each month and show it using a scatter plot
Also, add a grid in the plot. gridline style should “–“.'''
df = pd.read_csv(data_directory)
monthList = df['month_number'].tolist()
toothPasteSalesData = df['toothpaste'].tolist()
plt.scatter(monthList, toothPasteSalesData, label='Tooth paste Sales data')
plt.xlabel('Month Number')
plt.ylabel('Number of units Sold')
plt.legend(loc='upper left')
plt.title('Tooth paste Sales data')
plt.xticks(monthList)
plt.grid(True, linewidth=1, linestyle="--")
plt.show()

fig4 = go.Figure()
fig4.add_trace(go.Scatter(x=monthList, y=toothPasteSalesData, mode='markers', name='Toothpaste Sales Data'))
fig4.update_layout(title='Toothpaste Sales data', xaxis_title='Month Number', yaxis_title='Number of units Sold')


'''Exercise 5: Read face cream and facewash product sales data and show it using the bar chart
The bar chart should display the number of units sold per month for each product. Add a separate bar for each product in the same chart.'''
df = pd.read_csv(data_directory)
monthList = df['month_number'].tolist()
faceCremSalesData = df['facecream'].tolist()
faceWashSalesData = df['facewash'].tolist()

plt.bar([a-0.25 for a in monthList], faceCremSalesData, width=0.25, label='Face Cream sales data', align='edge')
plt.bar([a+0.25 for a in monthList], faceWashSalesData, width=-0.25, label='Face Wash sales data', align='edge')
plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.legend(loc='upper left')
plt.title(' Sales data')

plt.xticks(monthList)
plt.grid(True, linewidth= 1, linestyle="--")
plt.title('Facewash and facecream sales data')
plt.show()

fig5 = go.Figure()
fig5.add_trace(go.Bar(x=monthList, y=faceCremSalesData, name='Face Cream sales data'))
fig5.add_trace(go.Bar(x=monthList, y=faceWashSalesData, name='Face Wash sales data'))
fig5.update_layout(title='Facewash and facecream sales data', xaxis_title='Month Number', yaxis_title='Sales units in number')

'''Exercise 6: Read sales data of bathing soap of all months and show it using a bar chart.'''
df = pd.read_csv(data_directory)
monthList = df['month_number'].tolist()
bathingsoapSalesData = df['bathingsoap'].tolist()
plt.bar(monthList, bathingsoapSalesData)
plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.title('Sales data')
plt.xticks(monthList)
plt.grid(True, linewidth=1, linestyle="--")
plt.title('bathingsoap sales data')
plt.show()
fig6 = go.Figure()
fig6.add_trace(go.Bar(x=monthList, y=bathingsoapSalesData, name='Bathing Soap sales data'))
fig6.update_layout(title='Bathingsoap sales data', xaxis_title='Month Number', yaxis_title='Sales units in number')



'''Exercise 7: Read the total profit of each month and show it using the histogram to see the most common profit ranges'''
df = pd.read_csv(data_directory)
profitList = df['total_profit'].tolist()
labels = ['low', 'average', 'Good', 'Best']
profit_range = [150000, 175000, 200000, 225000, 250000, 300000, 350000]
plt.hist(profitList, profit_range, label='Profit data')
plt.xlabel('profit range in dollar')
plt.ylabel('Actual Profit in dollar')
plt.legend(loc='upper left')
plt.xticks(profit_range)
plt.title('Profit data')
plt.show()
fig7 = go.Figure()
fig7.add_trace(go.Histogram(x=profitList, xbins=dict(start=min(profit_range), end=max(profit_range), size=30000),
                            name='Profit data', autobinx=True))
fig7.update_layout(title='Profit data', xaxis_title='profit range in dollar', yaxis_title='Actual Profit in dollar')


'''Exercise 9: Read Bathing soap facewash of all months and display it using the Subplot'''
df = pd.read_csv(data_directory)
monthList = df['month_number'].tolist()
bathingsoap = df['bathingsoap'].tolist()
faceWashSalesData = df['facewash'].tolist()

f, axarr = plt.subplots(2, sharex=True)
axarr[0].plot(monthList, bathingsoap, label='Bathingsoap Sales Data', color='k', marker='o', linewidth=3)
axarr[0].set_title('Sales data of  a Bathingsoap')
axarr[1].plot(monthList, faceWashSalesData, label='Face Wash Sales Data', color='r', marker='o', linewidth=3)
axarr[1].set_title('Sales data of  a facewash')

plt.xticks(monthList)
plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.show()

fig9 = make_subplots(rows=2, cols=1, shared_xaxes=True)
fig9.add_trace(go.Scatter(x=monthList, y=bathingsoapSalesData, mode='lines+markers', name='Bathingsoap Sales Data'), row=1, col=1)
fig9.add_trace(go.Scatter(x=monthList, y=faceWashSalesData, mode='lines+markers', name='Face Wash Sales Data'), row=2, col=1)
fig9.update_layout(title='Sales data of a Bathingsoap and a facewash', xaxis_title='Month Number', yaxis_title='Sales units in number')


'''Exercise Question 10: Read all product sales data and show it using the stack plot'''
df = pd.read_csv(data_directory)
monthList = df['month_number'].tolist()

faceCremSalesData = df['facecream'].tolist()
faceWashSalesData = df['facewash'].tolist()
toothPasteSalesData = df['toothpaste'].tolist()
bathingsoapSalesData = df['bathingsoap'].tolist()
shampooSalesData = df['shampoo'].tolist()
moisturizerSalesData = df['moisturizer'].tolist()

plt.plot([],[],color='m', label='face Cream', linewidth=5)
plt.plot([],[],color='c', label='Face wash', linewidth=5)
plt.plot([],[],color='r', label='Tooth paste', linewidth=5)
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
fig10.add_trace(go.Scatter(x=monthList, y=faceCremSalesData, stackgroup='one', fill='tozeroy', name='face Cream'))
fig10.add_trace(go.Scatter(x=monthList, y=faceWashSalesData, stackgroup='one', fill='tonexty', name='Face wash'))
fig10.add_trace(go.Scatter(x=monthList, y=toothPasteSalesData, stackgroup='one', fill='tonexty', name='Tooth paste'))
fig10.add_trace(go.Scatter(x=monthList, y=bathingsoapSalesData, stackgroup='one', fill='tonexty', name='Bathing soap'))
fig10.add_trace(go.Scatter(x=monthList, y=shampooSalesData, stackgroup='one', fill='tonexty', name='Shampoo'))
fig10.add_trace(go.Scatter(x=monthList, y=moisturizerSalesData, stackgroup='one', fill='tonexty', name='Moisturizer'))
fig10.update_layout(title='All product sales data using stack plot', xaxis_title='Month Number', yaxis_title='Sales units in Number')

# Create a subplot with all the plots
fig = make_subplots(rows=5, cols=2, subplot_titles=("Company Profit per Month",
                                                  "Company Sales Data of Last Year",
                                                  "Sales Data of each Product",
                                                  "Toothpaste Sales Data",
                                                  "Facewash and Facecream Sales Data",
                                                  "Bathingsoap Sales Data",
                                                  "Profit Data",
                                                  "Sales Data of Bathingsoap and Facewash",
                                                  "All Product Sales Data using Stack Plot"),
                        shared_xaxes=False
)


# Add each plot to the subplot
#fig1
fig.add_trace(fig1.data[0], row=1, col=1)
#fig2
fig.add_trace(fig2.data[0], row=1, col=2)
#fig3
fig.add_trace(fig3.data[0], row=2, col=1)
fig.add_trace(fig3.data[1], row=2, col=1)
fig.add_trace(fig3.data[2], row=2, col=1)
fig.add_trace(fig3.data[3], row=2, col=1)
fig.add_trace(fig3.data[4], row=2, col=1)
fig.add_trace(fig3.data[5], row=2, col=1)
#fig4
fig.add_trace(fig4.data[0], row=2, col=2)
#fig5
fig.add_trace(fig5.data[0], row=3, col=1)
fig.add_trace(fig5.data[1], row=3, col=1)
#fig6
fig.add_trace(fig6.data[0], row=3, col=2)
#fig7
fig.add_trace(fig7.data[0], row=4, col=1)
#fig9
fig.add_trace(fig9.data[0], row=4, col=2)
fig.add_trace(fig9.data[1], row=4, col=2)
#fig10
fig.add_trace(fig10.data[0], row=5, col=1)
fig.add_trace(fig10.data[1], row=5, col=1)
fig.add_trace(fig10.data[2], row=5, col=1)
fig.add_trace(fig10.data[3], row=5, col=1)
fig.add_trace(fig10.data[4], row=5, col=1)
fig.add_trace(fig10.data[5], row=5, col=1)


# Update the layout of each subplot to include x-axis and y-axis titles
fig.update_xaxes(title_text='Month Number', row=1, col=1)
fig.update_yaxes(title_text='Profit in Dollar', row=1, col=1)

# Update the layout of Exercise 2 subplot
fig.update_xaxes(title_text='Month Number', row=1, col=2)
fig.update_yaxes(title_text='Profit in Dollar', row=1, col=2)

# Update the layout of Exercise 3 subplot
fig.update_xaxes(title_text='Month Number', row=2, col=1)
fig.update_yaxes(title_text='Sales Units in Number', row=2, col=1)

# Update the layout of Exercise 4 subplot
fig.update_xaxes(title_text='Month Number', row=2, col=2)
fig.update_yaxes(title_text='Number of Units Sold', row=2, col=2)

# Update the layout of Exercise 5 subplot
fig.update_xaxes(title_text='Month Number', row=3, col=1)
fig.update_yaxes(title_text='Sales Units in Number', row=3, col=1)

# Update the layout of Exercise 6 subplot
fig.update_xaxes(title_text='Month Number', row=3, col=2)
fig.update_yaxes(title_text='Sales Units in Number', row=3, col=2)

# Update the layout of Exercise 7 subplot
fig.update_xaxes(title_text='Profit Range in Dollar', row=4, col=1)
fig.update_yaxes(title_text='Actual Profit in Dollar', row=4, col=1)

# Update the layout of Exercise 9 subplot
fig.update_xaxes(title_text='Month Number', row=4, col=2)
fig.update_yaxes(title_text='Sales Units in Number', row=4, col=2)

# Update the layout of Exercise 10 subplot
fig.update_xaxes(title_text='Month Number', row=5, col=1)
fig.update_yaxes(title_text='Sales Units in Number', row=5, col=1)


# Update the layout of the subplot
fig.update_layout(height=1000, title_text="Interactive Plotly Visualizations for Company Sales Data")

# Save the combined plot as an HTML file
fig.write_html('combined_plots.html')
