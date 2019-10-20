#! -*- utf-8 -*-
# import pandas as pd
import plotly.graph_objects as go
#
# fig = go.Figure(data=go.Bar(y=[2,3,1]))
# fig.write_html('first_picture.html',auto_open=True)
"""
import plotly.express as px
iris = px.data.iris()
fig = px.scatter(iris, x="sepal_width", y="sepal_length", color="species")
fig.show()
print(fig['data'])
"""
from plotly.subplots import make_subplots
fig = make_subplots(rows=1, cols=2)
fig.add_trace(go.Scatter(y=[4, 2, 1], mode="lines"),row=1, col=1)
fig.add_trace(go.Bar(y=[2, 1, 3]), row=1, col=2)
fig.show()