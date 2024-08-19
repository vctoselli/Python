import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('C:\WebDev\PYTHON\FreeCodeCamp Data Analysis\Sea Level Predictor\epa-sea-level.csv', index_col='Year')

    # Create scatter plot
    scatter_fig = plt.subplots(figsize=(16,8))
    plt.scatter(x=df.index, y=df['CSIRO Adjusted Sea Level'])   

    # Create first line of best fit
    future_years = np.arange(df.index.min(), 2050)
    linear_regression_all_time = linregress(x=df.index, y=df['CSIRO Adjusted Sea Level'])
    predicted_sea_levels = linear_regression_all_time.slope * future_years + linear_regression_all_time.intercept
    plt.plot(future_years, predicted_sea_levels, label='Best Fit Line', color='red')    

    # Create second line of best fit
    years_2000_2050 = np.arange(2000,2050)
    df_2000_onwards = df[df.index >= 2000]
    linear_regression_2000 = linregress(x=df_2000_onwards.index, y= df_2000_onwards['CSIRO Adjusted Sea Level'])
    predicted_sea_levels_2000_onwards = linear_regression_2000.slope * years_2000_2050 + linear_regression_2000.intercept
    plt.plot(years_2000_2050, predicted_sea_levels_2000_onwards, label='Second Best Fit Line', color='green')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.grid(True)
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()