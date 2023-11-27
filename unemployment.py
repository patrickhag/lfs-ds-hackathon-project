import pandas as pd
import streamlit as st
import plotly.express as px
from st_btn_select import st_btn_select

drop_columns = ["Urban", "Rural"]
selection = "Chart"
select = None


@st.cache_data
def load_data():
    return pd.read_excel("RLFS_2022_Data_clean.xlsx", sheet_name="Table 0").iloc[1:]


selection = st_btn_select(("Chart", "Data"))


def render(data, select=""):
    drop_columns = []
    if select == "Residence":
        drop_columns = ["Male", "Female"]
    if select == "gender":
        drop_columns = ["Urban", "Rural"]
    return data.drop(columns=drop_columns, axis=0)


def main():
    data = load_data()

    if selection == "Data":
        select = st.radio("Filter data based on your need:", ("Residence", "gender"))
        st.write(render(data, select))
    elif selection == "Chart":
        select = st.radio("Filter data based on your need:", ("Percentage(%)", "Total"))

        processed_data = render(data)
        fig = px.bar(
            data_frame=processed_data,
            x="Indicators",
            y=select,
            height=500,
            title="Youth unemployment rate by education level",
        )
        if select == "Total":
            fig.update_traces(texttemplate="%{y:,}", textposition="outside")
        else:
            fig.update_layout(yaxis_range=[0, 100])
            fig.update_traces(texttemplate="%{y:.2f}%", textposition="outside")

        st.plotly_chart(fig)


main()
