import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

rand = np.random.randn(1000)
fig = px.histogram(rand)
st.write('histogram')
st.plotly_chart(fig)

df = px.data.tips()
st.write('bar chart')
st.plotly_chart(px.bar(df, x= 'day', y= 'total_bill', color= 'sex', barmode= 'group'))
