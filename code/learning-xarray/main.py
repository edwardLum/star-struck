import os
import xarray as xr
import matplotlib.pyplot as plt

import matplotlib.dates as mdates

# Exercise 1
def load_dataset(file_path):
    ds = xr.open_dataset(file_path, engine='cfgrib')

    return ds



def plot_time_series(ds, location):

    lat_min, lat_max = location['latitude']
    lon_min, lon_max = location['longitude']

    subset = ds.t2m.sel(latitude=slice(lat_min, lat_max), longitude=slice(lon_min, lon_max))

    spatial_mean = subset.mean(dim=['latitude', 'longitude'])
    daily_mean_temp = spatial_mean.mean(dim=['step'])

    daily_mean_temp.plot.line()

    # Use plt.gca() (Get Current Axes) to get the axes object and then modify it
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=2))  # Set major ticks every second day
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))  # Set format
    plt.gcf().autofmt_xdate() # autoformat the x-axis for better readability
    plt.xticks(rotation=45)  # Rotate labels for readability
    
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)

    plt.title('Mean temperature over time')
    plt.ylabel('Temperature (Kelvin)')
    plt.show()

if __name__ == "__main__":
    home_dir = os.path.expanduser('~')
    file_path = os.path.join(home_dir, 'Code/star-struck/data/download.grib')

    ds = load_dataset(file_path)
    # Define Attica region
    lat_min, lat_max = 38.25, 37.70 
    lon_min, lon_max = 23.45, 24.25

    location = {'latitude': (lat_min, lat_max),
                'longitude': (lon_min, lon_max)}
    
    plot_time_series(ds, location)
