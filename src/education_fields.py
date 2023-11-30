import streamlit as st
import pandas as pd
import plotly.express as px

st.markdown(
    """
                    #### Youth unemployment rate by field of studies"""
)

Chart, Data = st.tabs(["Charts", "Data"])


@st.cache_data
def load_data():
    return pd.read_excel("assets/RLFS_2022_Data_clean.xlsx", sheet_name="Table 2")


df_sheet_2 = load_data()
dd = ["All", "Male", "Female"]
select = st.sidebar.radio("Filter data based on gender:", dd)
with Data:
    if select == "All":
        st.write(df_sheet_2)
    else:
        st.write(df_sheet_2.drop(columns=[select, "Total"]))
with Chart:
    if select == "All":
        st.markdown(
            """
                    #### Youth unemployment rate by field of studies"""
        )
        fig = st.bar_chart(
            data=df_sheet_2,
            y=["Male", "Female"],
            x="Field of Education",
            height=500,
            width=800,
        )
    else:
        fig = px.bar(
            data_frame=df_sheet_2,
            x=select,
            y="Field of Education",
            height=500,
            width=800,
            title="Youth unemployment rate by education level",
        )
        fig.update_traces(texttemplate="%{x:,}", textposition="outside")
        fig.update_layout(
            xaxis=dict(scaleanchor="y", scaleratio=1),
            yaxis=dict(scaleanchor="x", scaleratio=1),
        )
        st.plotly_chart(fig)
