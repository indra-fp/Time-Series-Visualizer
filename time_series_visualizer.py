import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv') #read CSV
df['date'] = pd.to_datetime(df['date']) #convert date column to datetime datatype
df = df.set_index('date') #set date column to index


#for some reason using date is resulting errors, so make date as the index, and refer date to index from now

# Clean data
df = df.loc[
(df['value']<= df['value'].quantile(0.975)) & 
(df['value']>= df['value'].quantile(0.025))]



def draw_line_plot():
    # Draw line plot

    fig, ax = plt.subplots(figsize = (20, 15))
    ax = sns.lineplot(data = df)
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
  
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot

    df_bar = df.copy()
  
    df_bar['year'] = df.index.year
    df_bar['month'] = df.index.month_name()
    df_bar.groupby(['year','month']).mean()
    df_bar = df_bar.reset_index()
    
  
    added_data = {'year': [2016, 2016, 2016, 2016], 'month': ['January', 'February', 'March', 'April'], 'value': [0,0,0,0]}

    
    df_bar = pd.concat([pd.DataFrame(added_data), df_bar])
    # Draw bar plot

    fig, ax = plt.subplots(figsize = (20,10))
    ax = sns.barplot(data = df_bar, x = 'year', y = 'value', hue = 'month')
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1,2, figsize = (30,15))
  
    sns.boxplot(data = df_box, x = 'year', y='value', ax=ax[0])
    ax[0].set_title('Year-wise Box Plot (Trend)')
    ax[0].set_xlabel('Year')
    ax[0].set_ylabel('Page Views')
    

    order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sns.boxplot(data = df_box, x = 'month', y='value', order = order, ax=ax[1])
    ax[1].set_title('Month-wise Box Plot (Seasonality)')
    ax[1].set_xlabel('Month')
    ax[1].set_ylabel('Page Views')
    
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
