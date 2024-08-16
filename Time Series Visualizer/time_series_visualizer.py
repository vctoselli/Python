import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import seaborn as sns
import numpy as np
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('C:\WebDev\PYTHON\FreeCodeCamp Data Analysis\Page View Time Series Visualizer\\fcc-forum-pageviews.csv', index_col='date')

# Clean data
bottom_quantile_value = df['value'].quantile(0.025)
top_quantile_value = df['value'].quantile(0.975)
df = df.loc[(df['value'] >= bottom_quantile_value) & (df['value'] <= top_quantile_value)]


def draw_line_plot():
    # Draw line plot
    df_line = df.copy()
    x = df_line.index
    y = df_line['value']

    line_plot_fig, ax = plt.subplots(figsize=(16,8))

    ax.plot(x, y, color='red')
    ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(1,7)))
    ax.xaxis.set_minor_locator(mdates.MonthLocator())
    ax.grid(True)

    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.tight_layout()
    plt.show()

    # Save image and return fig (don't change this part)
    line_plot_fig.savefig('line_plot.png')
    return line_plot_fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar.index = pd.to_datetime(df_bar.index)
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month

    df_grouped = df_bar.groupby(['year', 'month'])['value'].mean().round(1).unstack()
    df_grouped = df_grouped.rename(columns={1 : 'January', 2 : 'February', 3 : 'March', 4 : 'April', 5 : 'May', 6 : 'June', 7 : 'July', 8 : 'August', 9 : 'September', 10 : 'October', 11 : 'November', 12 : 'December'})
    df_grouped

    # Draw bar plot
    labels = df_grouped.index

    x = np.arange(len(labels)) # location of x ticks
    width = 0.03 # Bar width
    multiplier = 0 # Multiplier to shift next column to the right

    bar_plot_fig, ax = plt.subplots(figsize=(16, 8)) # Plot empty graph

    for month in df_grouped.columns:
        offset = width * multiplier
        rects = ax.bar(x + offset, df_grouped[month], width, label=month)
        multiplier += 1

    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend(loc='upper left', title='Month')
    bar_plot_fig.tight_layout()

    # Save image and return fig (don't change this part)
    bar_plot_fig.savefig('bar_plot.png')
    return bar_plot_fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    sns.color_palette()
    box_plot_fig, axs = plt.subplots(1,2, figsize=(16,8))

    sns.boxplot(ax=axs[0], x=df_box['year'], y=df_box['value'], hue=df_box['year'], palette='bright', flierprops={"marker" : "."})
    axs[0].set_title('Year-wise Box Plot (Trend)')
    axs[0].set_xlabel('Year')
    axs[0].set_ylabel('Page Views')

    sns.boxplot(ax=axs[1], x=df_box['month'], y=df_box['value'], hue=df_box['month'], flierprops={"marker" : "."})
    axs[1].set_title('Month-wise Box Plot (Seasonality)')
    axs[1].set_xlabel('Month')
    axs[1].set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    box_plot_fig.savefig('box_plot.png')
    return box_plot_fig
