import streamlit as st
import pandas as pd
from datetime import datetime
import time

ts = time.time()
date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
timestamp = datetime.fromtimestamp(ts).strftime("%H:%M:%S")

filename = f"Attendance_{date}.csv"  

df = pd.read_csv(filename)

st.dataframe(df.style.highlight_max(axis=0))

