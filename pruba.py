import streamlit as st
import pandas as pd
import pip
pip.main(['install','openpyx1'])


st.write("""
# My first app
Hello *world!*
""")

df = pd.read_csv("my_test.csv")

