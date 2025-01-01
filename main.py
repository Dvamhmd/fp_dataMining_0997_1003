#import library

import streamlit as st
from web_function import load_data

from Tabs import home, predict, visualize

Tabs = {
    "Home" : home,
    "Prediction" : predict,
    "Visualization" : visualize
}

#sidebar
st.sidebar.title("Navigasi")

#radio option
page = st.sidebar.radio("Pages", list(Tabs.keys()))

#load dataset
df, x, y = load_data()

#kondisi call app function
if page in ["Prediction", "Visualization"]:
    Tabs[page].app(df, x,y)
else:
    Tabs[page].app()