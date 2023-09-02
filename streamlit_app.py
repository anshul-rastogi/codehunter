import streamlit as st
import numpy as np
import pandas as pd

st.write("""
# My first app
Hello *world!*
""")
         
chart_data = pd.DataFrame(
    np.random.randn(20,3), columns=["a", "b", "c"]
)

map_data = pd.DataFrame(
    np.random.randn(1000,2) /[50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)

st.map(map_data)

st.line_chart(chart_data)
# df = pd.read_csv("my_data.csv")
# st.bar_chart(df)


