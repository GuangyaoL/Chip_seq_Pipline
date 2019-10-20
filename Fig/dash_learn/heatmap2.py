#! -*- utf-8 -*-
import pandas as pd

import dash_core_components as dcc
import dash_bio as dashbio
import warnings

df = pd.read_csv('https://raw.githubusercontent.com/plotly/dash-bio/master/tests/dashbio_demos/sample_data/clustergram_mtcars.tsv',
                 sep='\t', skiprows=4).set_index('model')

columns = list(df.columns.values)
rows = list(df.index)

clustergram = dashbio.Clustergram(
    data=df.loc[rows].values,
    row_labels=rows,
    column_labels=columns,
    color_threshold={
        'row': 250,
        'col': 700
    },
    height=800,
    width=700,
    color_list={
        'row': ['#636EFA', '#00CC96', '#19D3F3'],
        'col': ['#AB63FA', '#EF553B'],
        'bg': '#506784'
    },
    line_width=2
)
print(dcc.Graph(figure=clustergram))
# dcc.Graph(figure=clustergram)