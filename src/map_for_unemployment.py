import streamlit as st
import folium
from streamlit_folium import folium_static
import pandas as pd

df_sheet_8 = pd.read_excel('RLFS_2022_Data_clean.xlsx', sheet_name='Table 8')

districts_df = df_sheet_8.iloc[:, :5]

@st.cache_data()
def unemployment_according_to_location():
    st.write("<b>Overall unemployment accross districts</b>",
             unsafe_allow_html=True)
    m = folium.Map(location=[districts_df['lat'].mean(),
                   districts_df['lon'].mean()], zoom_start=9)
    for index, row in districts_df.iterrows():
        folium.Marker([row['lat'], row['lon']],
                      popup=f"District: {row['district']}\nUnemployment Rate: {row['rate']}%\nTotal: {row['total']:,.0f}"
                      ).add_to(m)
    folium_static(m)
