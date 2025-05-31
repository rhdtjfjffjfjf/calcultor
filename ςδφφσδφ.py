import streamlit as st
import pandas as pd
import numpy as np

st.title("My App")

st.header("Calculator")


y = st.number_input(label="Enter your 1 number")


x = st.number_input(label="Enter the 2 number")


opp = st.text_input(label='Enter the opperation')

if opp == "+":
    st.success(f"{y+x}")
if  opp == "-":
    st.success(f"{y-x}")
elif opp == "x":
    st.success(f"{y*x}")
elif opp == "/":
    if x == 0:
        st.warning("Cannot divide with 0")
    else:
        st.success(f"{y/x}")
else:
    st.info("Not Avaiable Opperation", icon='🚨')
    




