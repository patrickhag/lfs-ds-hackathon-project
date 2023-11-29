import pandas as pd
import streamlit as st
import plotly.express as px
import folium
from streamlit_folium import folium_static
from streamlit_option_menu import option_menu


st.set_page_config(page_title="Rwanda Labour Force Survey Dashboard", layout="wide")

st.subheader("Addressing Rwanda's Youth Jobs Challenge")

st.markdown("""---""")


# dataframes
df_sheet_1 = pd.read_excel("assets/RLFS_2022_Data_clean.xlsx", sheet_name="Table 0")
df_sheet_2 = pd.read_excel("assets/RLFS_2022_Data_clean.xlsx", sheet_name="Table 2")
df_sheet_3 = pd.read_excel("assets/RLFS_2022_Data_clean.xlsx", sheet_name="Table 3")
df_sheet_4 = pd.read_excel("assets/RLFS_2022_Data_clean.xlsx", sheet_name="Table 4")
df_sheet_7 = pd.read_excel("assets/RLFS_2022_Data_clean.xlsx", sheet_name="Table 7")
df_sheet_8 = pd.read_excel("assets/RLFS_2022_Data_clean.xlsx", sheet_name="Table 8")

districts_df = df_sheet_8.iloc[:, :5]
unemployed_youth_over = df_sheet_1.loc[0, "Total"]
unemployed_secondary_graduates = df_sheet_1.loc[4, "Total"]
unemployed_university_graduates = df_sheet_1.loc[5, "Total"]
youth_neet = df_sheet_1.loc[6, "Total"]


def charts_section():
    section_1, section_2 = st.columns([4, 4])

    with section_1:
        col1, col2 = st.columns(2, gap="small")
        with col1:
            st.info("Unemployment Youth(16-30) ages", icon="⬆")
            st.metric("th", value=f"{unemployed_youth_over:,.0f}")

            education_df = df_sheet_1.loc[
                df_sheet_1["Indicators"].isin(
                    [
                        "No education",
                        "Primary",
                        "Lower secondary",
                        "Upper secondary",
                        "University",
                    ]
                ),
                ["Indicators", "Percentage(%)"],
            ]
        # first_chart
        fig = px.bar(
            education_df,
            x="Indicators",
            y="Percentage(%)",
            labels={
                "Percentage(%)": "Unemployment rate(%)",
                "Indicators": "Educational level",
            },
            title="Unemployment rates by level of education",
            color="Indicators",
        )
        fig.update_layout(width=450)
        st.plotly_chart(fig)

        with col2:
            st.info("Unemployed Secondary Graduates", icon="⬆")
            st.metric("th", value=f"{unemployed_secondary_graduates:,.0f}")

    with section_2:
        col3, col4 = st.columns(2, gap="small")
        with col3:
            st.info("Unemployed University Graduates", icon="⬆")
            st.metric("th", value=f"{unemployed_university_graduates:,.0f}")

            negate_education = [
                "youth neets",
                "no education",
                "Primary",
                "Lower secondary",
                "Upper secondary",
                "University",
            ]
            neets_based_on_age = df_sheet_7[
                ~df_sheet_7["Category"].isin(negate_education)
            ]
            fig = px.pie(
                neets_based_on_age,
                names="Category",
                values="Total",
                title="Youth NEETs Rates based on ages",
            )
            fig.update_layout(width=450)
            st.plotly_chart(fig)

        with col4:
            st.info("Youth NEETs (not Employed or in Education)", icon="⬆")
            st.metric("milli", value=f"{youth_neet:,.0f}")


@st.cache_data()
def unemployment_according_to_location():
    st.write("<b>Overall unemployment accross districts</b>", unsafe_allow_html=True)
    m = folium.Map(
        location=[districts_df["lat"].mean(), districts_df["lon"].mean()], zoom_start=9
    )
    for index, row in districts_df.iterrows():
        folium.Marker(
            [row["lat"], row["lon"]],
            popup=f"District: {row['district']}\nUnemployment Rate: {row['rate']}%\nTotal: {row['total']:,.0f}",
        ).add_to(m)
    folium_static(m)


charts_section()

st.sidebar.markdown(
    """
                    #
                    #
                    #
                    #
                    #
                    #
                    #
                     Made with ❤️ by Data-pioneers """
)
