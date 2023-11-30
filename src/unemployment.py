import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(layout="wide")
RWANDAN_POPULATION = 13078028

drop_columns = ["Urban", "Rural"]
gender = ("Male", "Female")
select = None
age_selection = None
selected_area = None


@st.cache_data
def load_data_sheet_4():
    return pd.read_excel("assets/RLFS_2022_Data_clean.xlsx", sheet_name="Table 4")


df_sheet_4 = load_data_sheet_4()

charts, custom_chart, data_tables = st.tabs(
    ["Education levels", "Youth labour force", "Table of data"]
)


@st.cache_data
def load_data():
    return pd.read_excel("assets/RLFS_2022_Data_clean.xlsx", sheet_name="Table 0").iloc[
        1:
    ]


@st.cache_data
def render(data, select=""):
    drop_columns = []
    if select == "Residence":
        drop_columns = ["Male", "Female"]
    elif select == "gender":
        drop_columns = ["Urban", "Rural"]
    else:
        return data  # No need to drop columns if select is not "Residence" or "gender"
    return data.drop(columns=drop_columns, axis=0)


data = load_data()
unique_values = df_sheet_4["Yrs"].unique()
age_selection = st.sidebar.multiselect(
    "filter by age", options=unique_values, default=unique_values
)

with charts:
    col1, col2 = st.columns([1, 3.5])
    with col1:
        select = col1.radio(
            "Select data filter option:",
            ("Percentage(%)", "Total"),
            captions=[
                "Filter data based on percentage population",
                "Filter data based on total population",
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
        general_view = st.checkbox("General View", value=True)
        if not general_view:
            selected_area = st.radio("Filter by Area:", drop_columns)
            slct = st.radio("Filter gender:", gender)

    with col2:
        if general_view:
            st.bar_chart(
                df_sheet_4.loc[df_sheet_4["Yrs"].isin(age_selection)],
                x="Category",
                y="Total",
            )
        else:
            melted_df = pd.melt(
                df_sheet_4.loc[df_sheet_4["Yrs"].isin(age_selection)],
                id_vars=["Category", "Yrs"],
                value_vars=[selected_area, slct],
            )

            chart = px.bar(
                melted_df,
                x="Category",
                y="value",
                color="Yrs",
                title="Youth unemployment rate by labour force",
                labels={"value": "Total", "Yrs": "Years"},
                height=500,
                width=600,
                category_orders={"Yrs": sorted(df_sheet_4["Yrs"].unique())},
            )

            chart.update_layout(
                xaxis_title="Category",
                yaxis_title="Total",
                yaxis=dict(range=[0, RWANDAN_POPULATION]),
            )

            st.plotly_chart(chart, use_container_width=True)
with data_tables:
    col1, col2 = st.columns([1, 3.5])
    with col1:
        preview = st.checkbox("filter by education level")
        select = st.radio("Filter data based on your need:", ("Residence", "gender"))
    with col2:
        st.markdown("### Unemployment based on education level, gender and residence")
        if preview:
            st.write(render(data, select))
        else:
            st.write(
                render(df_sheet_4.loc[df_sheet_4["Yrs"].isin(age_selection)], select)
            )
        st.write(
            "Check or uncheck __filter by education level__ checkbox to view different datasets."
        )
