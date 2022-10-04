#!/home/mdettmann/transmittance/bin python

import plotly.graph_objects as go
from scipy.signal import savgol_filter
import os
from halo import Halo

spinner = Halo(text='Working...')
spinner.start()
folder = os.getcwd()
folders = [ f.name for f in os.scandir(folder) if f.is_dir() ]
folders.sort()
fig = go.Figure()
for folder in folders:
    power_file = f"{folder}/Power{folder}.txt"
    temperature_file = f"{folder}/Tdiss{folder}.txt"
    with open(power_file, 'r') as f:
        power_lines = f.readlines()
    with open(temperature_file, 'r') as f:
        temperature_lines = f.readlines()

    power_lines = power_lines[13:]
    powers = []
    for line in power_lines:
        parts = line.split()
        if len(parts) == 0:
            try:
                powers.append(float(line))
            except:
                pass
        else:
            powers.append(float(parts[0]))

    temperature_lines = temperature_lines[1:]
    dates = []
    times = []
    temperatures = []
    for line in temperature_lines:
        parts = line.split('\t')
        dates.append(parts[0])
        times.append(parts[1])
        temperatures.append(float(parts[2]))

    temperatures = temperatures[:len(powers)]
    window = len(powers)//20
    window = window + 1 if window % 2 == 0 else window
    smoothed = savgol_filter(powers, window ,3)

    high = max(smoothed)
    low = min(smoothed)

    smoothed = [(val - low) * (1/(high-low))*100 for val in smoothed]
    powers = [(val -low) * (1/(high-low))*100 for val in powers]


    # Save Data
    with open(f"{folder}/{folder}.csv", 'w') as f:
        f.writelines([f"{val[0]},{val[1]},{val[2]}\n" for val in list(zip(temperatures, powers, smoothed))])
    
    fig.add_trace(go.Scatter(x=temperatures, y=smoothed, mode='lines', name=folder))

fig.update_layout(
    xaxis_title="Temperature (\u00B0C)",
    yaxis_title="Power (W)")

# Create figure
fig.write_html("all_plots.html")

spinner.stop()

