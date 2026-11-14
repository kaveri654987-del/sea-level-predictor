# Sea Level Predictor

This Python data-analysis project visualizes historical global average sea-level change and uses linear regression to estimate sea level through 2050.

## What it does

- Loads `epa-sea-level.csv` with Pandas.
- Creates a scatter plot of Year against CSIRO Adjusted Sea Level.
- Uses `scipy.stats.linregress` to calculate a line of best fit using all available years.
- Fits a second line using data from 2000 onward.
- Extends both regression lines to 2050.
- Labels the chart and saves it as `sea_level_plot.png`.

## Files

- `sea_level_predictor.py` — analysis and plotting code.
- `requirements.txt` — required Python packages.
- `epa-sea-level.csv` — input dataset; download it separately from the freeCodeCamp Sea Level Predictor project resources.

## Setup

1. Download `epa-sea-level.csv` from the freeCodeCamp project resources.
2. Place the CSV file in the same folder as `sea_level_predictor.py`.
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run:

   ```bash
   python sea_level_predictor.py
   ```

The chart will be saved as `sea_level_plot.png`.

## Data source

Global Average Absolute Sea Level Change, 1880–2014, from the US Environmental Protection Agency using data from CSIRO (2015) and NOAA (2015).
