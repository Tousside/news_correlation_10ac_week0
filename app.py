import requests
import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title="Global News Dashboard", page_icon=":bar_chart", layout="wide")

#header
with st.container():
    st.subheader("Eplore global news")
    st.title("News Data Analysis")
    st.write("What I get as results")
# results

with st.container():
    st.write("---")
    left_column, right_column= st.columns(2)
    with left_column:
        st.title("Which are the hot topics?")
        st.write("##")
        st.image("doc/Topics.png", caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    with right_column:
       st.title("New medias organisations per country")
       st.image("doc/label1.png", caption=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
 
with st.container():
    st.write("---")
    left_column, right_column= st.columns(2)
    with left_column:
        st.title("Title sentiments")
        st.write("##")
        st.image("doc/sentiment.png", caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    with right_column:
        st.title("Topics publication over time")
        st.image("doc/Trends.png", caption=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
