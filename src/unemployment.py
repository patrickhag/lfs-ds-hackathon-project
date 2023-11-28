import pandas as pd
import streamlit as st
import plotly.express as px
import altair as alt

st.set_page_config(layout="wide")
RWANDAN_POPULATION = 13000000
drop_columns = ["Urban", "Rural"]
gender = ("Male", "Female")
select = None
age_selection = None
selected_area = None

df_sheet_4 = pd.read_excel("assets/RLFS_2022_Data_clean.xlsx", sheet_name="Table 4")

charts, custom_chart, data_tables = st.tabs(
    ["Education levels", "Youth labour force", "Table of data"]
)


@st.cache_data
def load_data():
    return pd.read_excel("assets/RLFS_2022_Data_clean.xlsx", sheet_name="Table 0").iloc[
        1:
    ]


def render(data, select=""):
    drop_columns = []
    if select == "Residence":
        drop_columns = ["Male", "Female"]
    if select == "gender":
        drop_columns = ["Urban", "Rural"]
    return data.drop(columns=drop_columns, axis=0)


data = load_data()
age_selection = st.sidebar.multiselect(
    "filter by age",
    options=df_sheet_4["Yrs"].unique(),
    default=df_sheet_4["Yrs"].unique(),
)

with charts:
    col1, col2 = st.columns([1, 3.5])
    with col1:
        select = col1.radio(
            "Filter data based on your need:",
            ("Percentage(%)", "Total"),
            captions=[
                "View chart based on percentage population",
                "View chart based on total population",
            ],
        )
    with col2:
        processed_data = render(data)
        fig = px.bar(
            data_frame=processed_data.drop(processed_data.index[-1]),
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
with custom_chart:
    col1, col2 = st.columns([1, 3.5])
    with col1:
        selected_area = st.radio("Filter by Area:", drop_columns)
        slct = st.radio("Filter gender:", gender)
    with col2:
        melted_df = pd.melt(
            df_sheet_4.loc[df_sheet_4["Yrs"].isin(age_selection)],
            id_vars=["Category", "Yrs"],
            value_vars=[selected_area, slct],
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
            .properties(
                width=alt.Step(60),
                height=500,
                title="Youth unemployment rate by labour force",
            )
            .configure_axis(
                titlePadding=20,
                labelPadding=10,
            )
        )

        st.altair_chart(chart, use_container_width=True)

with data_tables:
    col1, col2 = st.columns([1, 3.5])
    with col1:
        preview = st.checkbox("filter by education level")
        select = st.radio("Filter data based on your need:", ("Residence", "gender"))
    with col2:
        st.markdown(
            """
                    ### Unemployment based on education level, gender and residence
                    """
        )
        if preview:
            st.write(render(data, select))
        else:
            st.write(
                render(df_sheet_4.loc[df_sheet_4["Yrs"].isin(age_selection)], select)
            )
        st.write(
            """
            Check or uncheck __filter by education level__ checkbox to view different datasets.
            """
        )
