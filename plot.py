import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import plotly.express as px
import plotly.figure_factory as ff

st.header("altair scattaer plot")
df = pd.DataFrame(np.random.randn(100,5),columns=['a','b','c','d','e'])
chart = alt.Chart(df).mark_circle().encode(x='a',y='b',size='c',tooltip=['a','b','c','d','e'])
st.altair_chart(chart)

st.header("interactive charts")

df = pd.read_csv("lang_data.csv")
lang_list = df.columns.tolist()
lang_choice = st.multiselect("choose a language",lang_list)
new_df = df[lang_choice]
st.line_chart(new_df)
st.area_chart(new_df)


st.header("data visualisation with plotly")
df = pd.read_csv("tips.csv")
st.dataframe(df)

st.header('Pie chart')
fig = px.pie(df,values='total_bill',names="day")
st.plotly_chart(fig)

st.header('Pie chart with multiple properties ')
fig = px.pie(df,values='total_bill',names="day",opacity=0.7,color_discrete_sequence=px.colors.sequential.RdBu)
st.plotly_chart(fig)

# st.subheader("histogram")
# x1 = np.random.randn(200)
# x2 = np.random.randn(200)
# x3 = np.random.randn(200)
# hist_data = [x1,x2,x3]
# group_labels = ['group1','group2','group3']
# fig = ff.create_distplot(hist_data,group_labels,bin_size=[.1,.25,.5])
# st.plotly_chart(fig)