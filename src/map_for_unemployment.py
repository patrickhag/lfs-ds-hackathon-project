import streamlit as st
import pandas as pd
import geopandas as gpd
import plotly.express as px

st.set_page_config(layout="wide")

districts_df = pd.read_excel(
    "assets/RLFS_2022_Data_clean.xlsx", sheet_name="Table 8")

st.markdown('### Total Unemployment rate accross districts')

Map, Data = st.tabs(['Map', 'Data'])
with Map:
    shapefile_path = "assets/geo-json-data/rwa_adm2_2006_NISR_WGS1984_20181002.shp"
    gdf = gpd.read_file(shapefile_path)

    gdf.rename(columns={'ADM2_EN': 'Districts'}, inplace=True)
    merged_df = pd.merge(gdf, districts_df, on='Districts', how='left')

    fig = px.choropleth_mapbox(
        merged_df,
        geojson=gdf.geometry,
        locations=merged_df.index,
        color=merged_df.total,
        color_continuous_scale="Inferno",
        hover_name='Districts',
        mapbox_style="stamen-terrain",
        center={"lat": -1.9403, "lon": 29.8739},
        zoom=7.5,
    )

    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0}, width=900)

    st.plotly_chart(fig)
with Data:
    districts_df
