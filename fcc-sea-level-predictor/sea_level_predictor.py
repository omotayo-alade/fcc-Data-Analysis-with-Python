import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv', usecols=[0,1])
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    # Create scatter plot
    plt.scatter(x, y)

    # Create first line of best fit
    r1 = linregress(x, y)
    
    year_extended = np.arange(1880, 2050, 1)
    year_extended2 = np.arange(2000, 2050, 1)
    
    # Create second line of best fit
    df2 = df[df['Year'] >= 2000]
    x2 = df2['Year']
    y2 = df2['CSIRO Adjusted Sea Level']
    
    r2 = linregress(x2, y2)
    line1 = [r1.intercept + r1.slope*i for i in year_extended]
    line2 = [r2.intercept + r2.slope*i for i in year_extended2]
    
    plt.plot(year_extended, line1)
    plt.plot(year_extended2, line2)

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()