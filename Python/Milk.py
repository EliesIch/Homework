import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as ff

import numpy as np
import pandas as pd
import scipy
import peakutils

milk_data = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/datasets/master/monthly-milk-production-pounds.csv'
)
time_series = milk_data['Monthly milk production (pounds per cow)']
time_series = np.asarray(time_series)

df = milk_data[0:15]

table = ff.create_table(df)
py.iplot(table, filename='milk-production-dataframe')
baseline_values = peakutils.baseline(time_series)

x = [j for j in range(len(time_series))]
time_series = time_series.tolist()
baseline_values = baseline_values.tolist()

rev_baseline_values = baseline_values[:11]
rev_baseline_values.reverse()
area_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
area_y = time_series[:11] + rev_baseline_values

trace = go.Scatter(x=x,
                   y=time_series,
                   mode='lines',
                   marker=dict(color='#B292EA', ),
                   name='Original Plot')

trace2 = go.Scatter(x=x,
                    y=baseline_values,
                    mode='markers',
                    marker=dict(
                        size=3,
                        color='#EB55BF',
                    ),
                    name='Bassline')

trace3 = go.Scatter(x=area_x,
                    y=area_y,
                    mode='lines+markers',
                    marker=dict(
                        size=4,
                        color='rgb(255,0,0)',
                    ),
                    name='1st Peak Outline')

first_peak_x = [j for j in range(11)]
area_under_first_peak = np.trapz(time_series[:11], first_peak_x) - np.trapz(
    baseline_values[:11], first_peak_x)
area_under_first_peak

annotation = go.Annotation(
    x=80,
    y=1000,
    text='The peak integration for the first peak is approximately %s' %
    (area_under_first_peak),
    showarrow=False)

layout = go.Layout(annotations=[annotation])

trace_data = [trace, trace2, trace3]
fig = go.Figure(data=trace_data, layout=layout)
py.iplot(fig, filename='milk-production-peak-integration')