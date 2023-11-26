import pandas as pd
import streamlit as st
import plotly.express as px
from streamlit_option_menu import option_menu
from map_for_unemployment import unemployment_according_to_location

st.set_page_config(page_title='Rwanda Labour Force Survey Dashboard',
                   layout='wide')

st.subheader("Addressing Rwanda's Youth Jobs Challenge")

st.markdown("""---""")

# dataframes
df_sheet_1 = pd.read_excel('RLFS_2022_Data_clean.xlsx', sheet_name='Table 0')
df_sheet_2 = pd.read_excel('RLFS_2022_Data_clean.xlsx', sheet_name='Table 2')
df_sheet_3 = pd.read_excel('RLFS_2022_Data_clean.xlsx', sheet_name='Table 3')
df_sheet_4 = pd.read_excel('RLFS_2022_Data_clean.xlsx', sheet_name='Table 4')
df_sheet_7 = pd.read_excel('RLFS_2022_Data_clean.xlsx', sheet_name='Table 7')

unemployed_youth_over = df_sheet_1.loc[0, 'Total']
unemployed_secondary_graduates = df_sheet_1.loc[4, 'Total']
unemployed_university_graduates = df_sheet_1.loc[5, 'Total']
youth_neet = df_sheet_1.loc[6, 'Total']


selected_age = st.sidebar.multiselect(
    "Filter by age",
    options=df_sheet_4["Yrs"].unique(),
)
selected_area = st.sidebar.multiselect(
    "Filter by Area", ['Rural', 'Urban'])


def filter_data_location(selected_area):
    clean_data_set = df_sheet_1.copy()

    if 'Urban' in selected_area and 'Rural' in selected_area:
        clean_data_set
    elif 'Urban' in selected_area:
        clean_data_set = clean_data_set.drop(columns=['Rural'], axis=1)
    elif 'Rural' in selected_area:
        clean_data_set = clean_data_set.drop(columns=['Urban'], axis=1)

    return clean_data_set


df_selected_area = filter_data_location(selected_area)
df_selected_area

selected_gender = st.sidebar.radio(
    "Filter by gender",
    ['Male', 'Female'],
    index=None
)
selected_gender


def filter_based_gender(selected_gender):
    clean_data_set = df_sheet_1.copy()

    if 'Male' == selected_gender and 'Female' == selected_gender:
        clean_data_set
    if 'Male' == selected_gender:
        clean_data_set = clean_data_set.drop(columns=['Female'], axis=1)
    elif 'Female' == selected_gender:
        clean_data_set = clean_data_set.drop(columns=['Male'], axis=1)

    return clean_data_set


df_gender_data = filter_based_gender(selected_gender)
# df_gender_data


def charts_section():
    section_1, section_2 = st.columns([4, 4])

    with section_1:
        col1, col2 = st.columns(2, gap='small')
        with col1:
            st.info("Overall Unemployment Youth(16-30) ages", icon="⬆")
            st.metric('th', value=f'{unemployed_youth_over:,.0f}')

            education_df = df_sheet_1.loc[df_sheet_1['Indicators'].isin(
                ["No education", "Primary", "Lower secondary", "Upper secondary", "University"]), ["Indicators", "Percentage(%)"]]
        # first_chart
        fig = px.bar(
            education_df,
            x="Indicators",
            y="Percentage(%)",
            labels={"Percentage(%)": "Unemployment rate(%)",
                    "Indicators": "Educational level"},
            title="Unemployment rates by level of education",
            color="Indicators"
        )
        fig.update_layout(width=450)
        st.plotly_chart(fig)

        programs_df = df_sheet_2.iloc[:, :2]

        fig = px.line(
            programs_df,
            y="Total",
            x="Field of Education",
            title="Mostly likely Education took by Unemployed Youth",
        )
        fig.update_layout(width=450)
        st.plotly_chart(fig)
        with col2:
            st.info("Unemployed Secondary Graduates", icon="⬆")
            st.metric('th', value=f'{unemployed_secondary_graduates:,.0f}')

    with section_2:
        col3, col4 = st.columns(2, gap='small')
        with col3:
            st.info("Unemployed University Graduates", icon="⬆")
            st.metric('th', value=f'{unemployed_university_graduates:,.0f}')

            youth_neet_rates = df_sheet_7.loc[df_sheet_7['Category'].isin(
                ["Total", "Male", "Female", "Urban", "Rural", "Urban Male", "Rural Male", "Urban Female", "Rural Female"]), ["Category", "Total"]]
            fig = px.pie(
                youth_neet_rates,
                names='Category',
                values="Total",
                title="Youth NEETs Rates by Gender and Area",
            )
            fig.update_layout(width=450)
            st.plotly_chart(fig)

        st.write("<br><b>Youth who participated in subsistence agriculture<b>",
                 unsafe_allow_html=True)
        df_sheet_3

        with col4:
            st.info("Youth NEETs (not Employed or in Education)", icon="⬆")
            st.metric('milli', value=f'{youth_neet:,.0f}')


# sidebar
def sidebar_contents():
    with st.sidebar:
        selected = option_menu(
            menu_title="Navbar",
            options=["Charts", "Maps"],
            menu_icon="cast",
            default_index=0
        )
    if selected == "Charts":
        pass
        # charts_section()
    if selected == "Maps":
        unemployment_according_to_location()


sidebar_contents()
st.sidebar.markdown(""" Made with ❤️ by Data-pioneers """)
