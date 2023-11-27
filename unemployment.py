import pandas as pd
import streamlit as st

import plotly.express as px
from st_btn_select import st_btn_select

# st.subheader("Addressing Rwanda's Youth Jobs Challenge")
# def render(){}
# st.markdown("""---""")
selection = st_btn_select(("Chart", "Data"))
select = "Demographics"
# dataframes
df_sheet_1 = pd.read_excel("RLFS_2022_Data_clean.xlsx", sheet_name="Table 0")
drop_columns = ["Urban", "Rural"]
select = st_btn_select(("Demographics", "gender"))
# data = df_sheet_1.drop(columns=drop_columns, axis=0)


def render():
    if select == "Demographics":
        drop_columns = ["Urban", "Rural"]
        return df_sheet_1.drop(columns=drop_columns, axis=0)
    if select == "gender":
        drop_columns = ["Male", "Female"]
        return df_sheet_1.drop(columns=drop_columns, axis=0)


if selection == "Data":
    # render()
    st.write(render())
if selection == "Chart":
    data = render()
    st.write(data)
    st.write(px.bar(data, x="Indicators", y="Total"))
