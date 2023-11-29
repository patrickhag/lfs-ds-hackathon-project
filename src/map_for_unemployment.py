import streamlit as st
import folium
from streamlit_folium import folium_static
import pandas as pd

st.set_page_config(layout="wide")

df_sheet_8 = pd.read_excel("assets/RLFS_2022_Data_clean.xlsx", sheet_name="Table 8")

districts_df = df_sheet_8.iloc[:, :5]


@st.cache_data()
def unemployment_according_to_location():
    st.write("<b>Overall unemployment accross districts</b>", unsafe_allow_html=True)
    m = folium.Map(
        location=[districts_df["lat"].mean(), districts_df["lon"].mean()],
        zoom_start=9,
    )
    for _, row in districts_df.iterrows():
        folium.Marker(
            [row["lat"], row["lon"]],
            popup=f"District: {row['district']}\nUnemployment Rate: {row['rate']}%\nTotal: {row['total']:,.0f}",
        ).add_to(m)
    folium_static(m)


unemployment_according_to_location()
# center on Liberty Bell, add marker
m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
folium.Marker(
    [39.949610, -75.150282], popup="Liberty Bell", tooltip="Liberty Bell"
).add_to(m)

# call to render Folium map in Streamlit
st_data = folium_static(m, width=725)
