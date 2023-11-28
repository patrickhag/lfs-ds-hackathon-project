import pandas as pd
import streamlit as st


def filter_data_location(selected_area, df):
    clean_data_set = df.copy()

    if "Urban" in selected_area and "Rural" in selected_area:
        clean_data_set
    elif "Urban" in selected_area:
        clean_data_set = clean_data_set.drop(columns=["Rural"], axis=1)
    elif "Rural" in selected_area:
        clean_data_set = clean_data_set.drop(columns=["Urban"], axis=1)

    return clean_data_set


def filter_data_gender(gender, df):
    clean_data_set = df.copy()

    if gender == "Male":
        clean_data_set = clean_data_set.drop(columns=["Female", "Total"], axis=1)
    if gender == "Female":
        clean_data_set = clean_data_set.drop(columns=["Male", "Total"], axis=1)

    return clean_data_set


def filter_data_age(selected_age, df):
    return df.loc[df["Yrs"].isin(selected_age)]


def filter(df, select, selected_age, selected_area):
    df = filter_data_gender(select, df)
    df = filter_data_age(selected_age, df)
    return filter_data_location(selected_area, df)
