import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df=pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    slope, y_intercept = linregress(df['Year'],df['CSIRO Adjusted Sea Level'])[:2]
    x = np.array(range(df['Year'][0],2051,1))
    y = y_intercept + slope*x
    plt.plot(x,y)

    # Create second line of best fit
    mask = df['Year'] >= 2000
    slope, y_intercept = linregress(df['Year'].loc[mask],df['CSIRO Adjusted Sea Level'].loc[mask])[:2]
    x = np.array(range(2000,2051,1))
    y = y_intercept + slope*x
    plt.plot(x,y)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()