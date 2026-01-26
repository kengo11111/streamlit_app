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

# 年度と地域は識別用の列として保持する
id_cols = ['調査年', '地域']

# Mから始まる列（性別・年齢層ごとの平均時間）だけを抽出する
value_cols = [c for c in df.columns if c.startswith('M')]

# melt を利用し、講義で扱った資料のように横に並んだ年齢層・性別ごとの平均時間の列を横に並んだ指標列を1列にまとめて縦持ちデータに変換する
df_long = df.melt(
    id_vars=id_cols,
    value_vars=value_cols,
    var_name='raw_col',
    value_name='minutes'
)