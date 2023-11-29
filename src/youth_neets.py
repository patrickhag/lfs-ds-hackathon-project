import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")


st.info("Youth NEET(not in employment, education or training)")

Charts, Data = st.tabs(["Charts", "Data"])

df_sheet_7 = pd.read_excel("assets/RLFS_2022_Data_clean.xlsx", sheet_name="Table 7")

negate_age = ["youth neets", "16-19 yrs", "20-24 yrs", "25-30 yrs"]
neets_based_on_education = df_sheet_7[~df_sheet_7["Category"].isin(negate_age)]

negate_education = [
    "youth neets",
    "no education",
    "Primary",
    "Lower secondary",
    "Upper secondary",
    "University",
]
neets_based_on_age = df_sheet_7[~df_sheet_7["Category"].isin(negate_education)]


with Charts:
    left_side, right_side = st.columns(2)
    with left_side:
        fig = px.pie(
            neets_based_on_education,
            names="Category",
            values="Total",
            title="Youth NEETs Rates based on education",
        )
        fig.update_layout(width=450)
        st.plotly_chart(fig)

    with right_side:
        fig = px.pie(
            neets_based_on_age,
            names="Category",
            values="Total",
            title="Youth NEETs Rates based on ages",
        )
        fig.update_layout(width=450)
        st.plotly_chart(fig)

    gender, residence = st.tabs(["filter based on gender", "Rular, urban and gender"])

    with gender:
        columns = list(["Category", "Male", "Female"])
        st.markdown("### Youth NEETs Rates based on education")
        st.bar_chart(
            df_sheet_7[df_sheet_7["Category"].isin(negate_education)][columns].loc[1:],
            x="Category",
            y=["Male", "Female"],
        )

    with residence:
        columns = list(
            [
                "Category",
                "Urban Male",
                "Urban Female",
                "Rural Male",
                "Rural Female",
            ]
        )
        st.markdown("### Youth NEETs Rates based on education ,Rular, urban and gender")
        st.area_chart(
            df_sheet_7[df_sheet_7["Category"].isin(negate_education)][columns].loc[1:],
            x="Category",
            y=[
                "Urban Male",
                "Urban Female",
                "Rural Male",
                "Rural Female",
            ],
            height=500,
        )

with Data:
    df_sheet_7
