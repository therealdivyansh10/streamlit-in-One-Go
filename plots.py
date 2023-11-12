import streamlit as st
import pandas  as pd
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns

chart_data = pd.DataFrame(np.random.randn(20,3),columns=['line1','line2','line3'])
st.subheader("line_chart")
st.line_chart(chart_data)

st.subheader('area chart')
st.area_chart(chart_data)
st.bar_chart(chart_data )

df = pd.read_csv("iris.csv")
st.dataframe(df)
fig = plt.figure(figsize = (15,8))
df["species"].value_counts().plot(kind='bar')
st.pyplot(fig)

st.subheader("seaborn")
fig = plt.figure(figsize=(15,8))
sns.distplot(df["sepal_length"])
st.pyplot(fig)

col1,col2 = st.columns(2)
with col1:
    col1.header("kde")
    fig = plt.figure()
    sns.set_style("darkgrid")
    sns.set_context('notebook')
    sns.kdeplot(df["sepal_length"])
    st.pyplot(fig)
    
with col2:
    col2.header("distplot")
    fig = plt.figure()
    sns.set_theme(context='poster',style="darkgrid")
    sns.displot(df["sepal_length"],kde="False")
    st.pyplot(fig)


st.subheader("scatter plot")
fig,ax = plt.subplots(figsize=(15,8))
ax.scatter(*np.random.random(size=(2,100)))
st.pyplot(fig)

st.subheader("Count plot")
fig = plt.figure(figsize=(10,7))
sns.countplot(data = df,x="species")
st.pyplot(fig)

# st.subheader("box plot")
# fig = plt.figure(figsize=(10,7))
# sns.boxplot(data=df, x= "species",y="petal_length")
# st.pyplot()

st.subheader("Violon plot")
fig = plt.figure(figsize=(10,7))
sns.violinplot(data = df,x="species",y="petal_length")
st.pyplot(fig)
