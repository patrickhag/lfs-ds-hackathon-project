import streamlit as st
from streamlit_folium import folium_static
import pandas as pd
from st_btn_select import st_btn_select
import plotly.express as px

selection = st_btn_select(("Chart", "Data"))
df_sheet_2 = pd.read_excel("RLFS_2022_Data_clean.xlsx", sheet_name="Table 2")
dd = ["Male", "Female", "All"]
select = st.radio("Filter data based on gender:", dd)
if selection == "Data":
    if select == "All":
        st.write(df_sheet_2)
    else:
        st.write(df_sheet_2.drop(columns=[select, "Total"]))
elif select != "All":
    dd.pop()
    fig = px.bar(
        data_frame=df_sheet_2,
        x=select,
        y="Field of Education",
        height=500,
        width=800,
        title="Youth unemployment rate by education level",
    )
    fig.update_traces(texttemplate="%{x:,}", textposition="outside")
    st.plotly_chart(fig)
