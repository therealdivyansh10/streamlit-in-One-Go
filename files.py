import streamlit as st

st.header("Loading the csv file")
df = st.file_uploader("Upload the csv file",type=["csv","xls"])

if df is not None:
    st.dataframe(df)

img = st.file_uploader("enter the image" )
if img is not None:
    st.image(img)