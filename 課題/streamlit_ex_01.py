import streamlit as st
import pandas as pd
import plotly.express as px

st.title('広告費と売り上げ')

df = pd.read_csv('ad_expense_sales.csv')

with st.sidebar:
    st.subheader('抽出条件')
    prod = st.multiselect(
        '製品カテゴリーを選択してください（複数選択可）',
        df['prod_category'].unique()
    )

    media = st.selectbox(
        '広告媒体を選択してください',
        df['media'].unique()
    )

    st.subheader('色分け')
    color = st.selectbox(
        '分類を選択してください',
        ['性別', '季節', '年齢']
    )

df = df[df['prod_category'].isin(prod)]
df = df[df['media'] == media]

if color == '性別':
    color_col = 'sex'
elif color == '季節':
    color_col = 'season'
elif color == '年齢':
    color_col = 'age'

compare_df = df[['sales','ad_expense']]
compare_df = compare_df.rename(columns={
    'sales': '売り上げ（円）',
    'ad_expense': '広告費（円）'
})
compare_df.index.name = '番号'
st.subheader('広告費と売り上げの関係（表）')
st.dataframe(compare_df,width=800, height=220)

st.subheader('広告費と売り上げの関係（散布図）')
fig = px.scatter(df,
                 x='ad_expense',
                 y='sales',
                 labels={
                     'ad_expense': '広告費（円）',
                     'sales': '売り上げ（円）'
                 },
                 color=color_col,   
                )
st.plotly_chart(fig)