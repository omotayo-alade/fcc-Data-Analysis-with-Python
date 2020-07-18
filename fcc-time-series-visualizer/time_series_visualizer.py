import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = None

# Clean data
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=[0], index_col=[0])

df = df.loc[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]
def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize=(18,6))
    plt.plot(df, color='red')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    fig = plt.gcf()

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.groupby([df.index.year, df.index.month]).agg({'value':'mean'})
    df_bar.index.names = ['Years', 'Months']
    df_bar.reset_index(inplace=True)
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    df_bar['Months'].replace([i for i in range(1,13)], [i for i in months], inplace=True) 

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(12,10))
    sns.barplot(x='Years', y='value', hue='Months', hue_order=months, data=df_bar, ax=ax)
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(loc='upper left')
    fig = plt.gcf()

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
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(20,6))
    sns.boxplot(x='year', y='value', data=df_box, ax=ax1)
    sns.boxplot(x='month', y='value', data=df_box, order=months, ax=ax2)
    ax1.set_title('Year-wise Box Plot (Trend)'), ax1.set_xlabel('Year'), ax1.set_ylabel('Page Views')
    ax2.set_title('Month-wise Box Plot (Seasonality)'), ax2.set_xlabel('Month'), ax2.set_ylabel('Page Views')
    fig = plt.gcf()

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
