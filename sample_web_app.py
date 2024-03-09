import  streamlit  as st
import pandas as pd

st.title("Sample Web App")
uplod_file = st.file_uploader('UPLOD')

if uplod_file is not None:
    st.write(pd.read_excel(uplod_file))