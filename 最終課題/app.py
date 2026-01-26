import streamlit as st
import pandas as pd
import plotly.express as px
import re

st.title('時間使用調査（活動別・性別・年齢層）')

activity = st.sidebar.selectbox(
    '活動種別を選択してください',
    ['Primary', 'Secondary', 'Tertiary']
)

df = pd.read_csv(f'{activity}.csv', encoding='shift_jis')

