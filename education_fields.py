import streamlit as st
from streamlit_folium import folium_static
import pandas as pd
import plotly.express as px

# import numpy as np

# chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["col1", "col2", "col3"])

# st.bar_chart(
#     chart_data, x="col1", y=["col2", "col3"], color=["#FF0000", "#0000FF"]  # Optional
# )

Chart, Data = st.tabs(["Charts", "Table of ata"])
df_sheet_2 = pd.read_excel("RLFS_2022_Data_clean.xlsx", sheet_name="Table 2")
dd = ["Male", "Female", "All"]
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
                    #### Youth eunemployment rate by field of studies"""
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
