import streamlit as st
import numpy as np
import pandas as pd


st.title('Streamlit 【入門編】')

st.write('DataFrame')

df = pd.DataFrame({
     '1':[1,2,3,4],
     '2':[10,20,30,40],    
})

st.write(df)
