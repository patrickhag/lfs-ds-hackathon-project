import pandas as pd
import streamlit as st
import plotly.express as px
import altair as alt
from st_btn_select import st_btn_select
from pie import filter

drop_columns = ["Urban", "Rural"]
select = None
RWANDAN_POPULATION = 13000000


@st.cache_data
def load_data():
    return pd.read_excel("RLFS_2022_Data_clean.xlsx", sheet_name="Table 0").iloc[1:]


selection = st_btn_select(("Charts", "Data", "Customize chart"))


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
        select = st.sidebar.radio(
            "Filter data based on your need:", ("Residence", "gender")
        )
        st.write(render(data, select))
    elif selection == "Charts":
        select = st.sidebar.radio(
            "Filter data based on your need:", ("Percentage(%)", "Total")
        )
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
    if selection == "Customize chart":
        df_sheet_4 = pd.read_excel("RLFS_2022_Data_clean.xlsx", sheet_name="Table 4")

        selected_area = st.sidebar.radio("Filter by Area", ["Rural", "Urban"])
        select = st.sidebar.radio("Filter gender:", ("Male", "Female"))
        melted_df = pd.melt(
            df_sheet_4,
            id_vars=["Category", "Yrs"],
            value_vars=[selected_area, select],
        )

        chart = (
            alt.Chart(melted_df)
            .mark_bar()
            .encode(
                x=alt.X("Category:N", title="Category"),
                y=alt.Y(
                    "sum(value):Q",
                    title="Total",
                    scale=alt.Scale(domain=[0, RWANDAN_POPULATION]),
                ),
                color=alt.Color("Yrs:N", title="Years"),
            )
            .properties(width=alt.Step(60), height=500)
            .configure_axis(
                titlePadding=20,
                labelPadding=10,
            )
        )

        st.altair_chart(chart, use_container_width=True)


main()
