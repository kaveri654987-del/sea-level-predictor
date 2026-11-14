import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
from pathlib import Path


def draw_plot():
    # Load the dataset from the same directory as this script.
    data_path = Path(__file__).with_name("epa-sea-level.csv")
    df = pd.read_csv(data_path)

    # Plot the original data.
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Regression line using all available years, extended to 2050.
    slope, intercept, r_value, p_value, std_err = linregress(
        df["Year"], df["CSIRO Adjusted Sea Level"]
    )
    years = pd.Series(range(1880, 2051))
    ax.plot(years, slope * years + intercept, label="Best fit: all years")

    # Regression line using data from 2000 onward, extended to 2050.
    recent_df = df[df["Year"] >= 2000]
    recent_slope, recent_intercept, r_value, p_value, std_err = linregress(
        recent_df["Year"], recent_df["CSIRO Adjusted Sea Level"]
    )
    recent_years = pd.Series(range(2000, 2051))
    ax.plot(
        recent_years,
        recent_slope * recent_years + recent_intercept,
        label="Best fit: 2000 onward",
    )

    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    ax.legend()

    # Save the chart and return the Axes object for the project tests.
    fig.savefig("sea_level_plot.png")
    return ax


if __name__ == "__main__":
    draw_plot()
