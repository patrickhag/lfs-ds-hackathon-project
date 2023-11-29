import streamlit as st
from st_btn_select import st_btn_select
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')


st.info("Youth NEET(not in employment, education or training)")


Charts, Data = st.tabs(['Charts', 'Data'])

df_sheet_7 = pd.read_excel("RLFS_2022_Data_clean.xlsx", sheet_name="Table 7")

age = st.sidebar.multiselect(
    "Filter by age",
    options=['16-24', '16-30'],
)

gender = st.sidebar.radio(
    "Filter by gender",
    ['Male', 'Female'],
    index=None
)

selected_region = st.sidebar.multiselect(
    "Filter by residence",
    options=['Urban', 'Rural'],
)


def filter_data_location(selected_region):
    global df_sheet_7
    if len(selected_region) == 0 or len(selected_region) == 2:
        return df_sheet_7
    elif 'Urban' in selected_region:
        dropped_col = df_sheet_7.drop(columns=['Rural Male', 'Rural Female'])
        st.write(dropped_col)
    elif 'Rural' in selected_region:
        return df_sheet_7.drop(columns=['Urban Male', 'Urban Female'])


filter_data_location(selected_region)


negate_age = ['youth neets', '16-19 yrs', '20-24 yrs', '25-30 yrs']
neets_based_on_education = df_sheet_7[~df_sheet_7['Category'].isin(
    negate_age)]

negate_education = ['youth neets', 'no education', 'Primary',
                    'Lower secondary', 'Upper secondary', 'University']
neets_based_on_age = df_sheet_7[~df_sheet_7['Category'].isin(
    negate_education)]

with Charts:
    left_side, right_side = st.columns(2)
    with left_side:
        fig = px.pie(
            neets_based_on_education,
            names='Category',
            values="Total",
            title="Youth NEETs Rates based on education",
        )
        fig.update_layout(width=400)
        st.plotly_chart(fig)

    with right_side:
        fig = px.pie(
            neets_based_on_age,
            names='Category',
            values="Total",
            title="Youth NEETs Rates based on ages",
        )
        fig.update_layout(width=400)
        st.plotly_chart(fig)
with Data:
    df_sheet_7
