import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    #df = df[df['Year'] >= 2000]
    #df = df.dropna()
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    fig, ax = plt.subplots(1, 1, figsize=(9,3))
    ax.scatter(x, y,label='original data')

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(x,y)
    final_point = 2051
    x2 = range(1880, final_point)
    ax.plot(x2, intercept + slope*x2, 'g', label='prediction')

    # Create second line of best fit
    df_last = df[df['Year'] >= 2000]
    df_last = df_last.dropna()
    x3 = df_last['Year']
    y3 = df_last['CSIRO Adjusted Sea Level']
    slope_last, intercept_last, r_value, p_value, std_err = linregress(x3, y3)
    x_last=range(2000,2051)
    ax.plot(x_last, intercept_last + slope_last*x_last, 'r', label='prediction 2000')


    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()