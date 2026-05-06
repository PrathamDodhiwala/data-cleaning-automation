import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import zscore


def handle_missing_values(df, strategy="mean"):
    for col in df.columns:
        if df[col].isnull().sum() > 0:
            if df[col].dtype in [np.float64, np.int64]:
                if strategy == "mean":
                    df[col].fillna(df[col].mean(), inplace=True)
                elif strategy == "median":
                    df[col].fillna(df[col].median(), inplace=True)
                else:
                    df[col].fillna(0, inplace=True)
            else:
                df[col].fillna(df[col].mode()[0], inplace=True)
    return df


def remove_duplicates(df):
    initial_shape = df.shape
    df = df.drop_duplicates()
    st.write(f"Removed {initial_shape[0] - df.shape[0]} duplicate rows")
    return df


def correct_column_types(df):
    for col in df.columns:
        try:
            df[col] = pd.to_numeric(df[col])
        except:
            pass
        try:
            df[col] = pd.to_datetime(df[col])
        except:
            pass
    return df


def strip_whitespace(df):
    str_cols = df.select_dtypes(include=["object"]).columns
    for col in str_cols:
        df[col] = df[col].str.strip()
    return df


def handle_outliers(df, threshold=3):
    num_cols = df.select_dtypes(include=[np.number]).columns
    if len(num_cols) > 0:
        z_scores = np.abs(df[num_cols].apply(zscore))
        df = df[(z_scores < threshold).all(axis=1)]
        st.write(f"Removed rows with outliers beyond {threshold} Z-score")
    return df


st.title("🧹 Data Cleaning Automation Tool")

uploaded_file = st.file_uploader("Upload claude_ai.csv", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### Original Data", df.head())
    st.write(f"Shape: {df.shape}")

    # Options for cleaning
    st.sidebar.header("Cleaning Options")
    missing_strategy = st.sidebar.selectbox(
        "Missing Value Strategy", ["mean", "median", "zero"]
    )
    remove_dupes = st.sidebar.checkbox("Remove Duplicates", value=True)
    strip_spaces = st.sidebar.checkbox("Strip Whitespace from Strings", value=True)
    fix_types = st.sidebar.checkbox("Auto-correct Column Types", value=True)
    remove_outliers = st.sidebar.checkbox("Remove Outliers (Z-score)", value=True)
    z_thresh = st.sidebar.slider("Z-score threshold", 2, 5, 3)

    if st.button("Clean Data"):
        # Cleaning process
        df = handle_missing_values(df, strategy=missing_strategy)
        if remove_dupes:
            df = remove_duplicates(df)
        if strip_spaces:
            df = strip_whitespace(df)
        if fix_types:
            df = correct_column_types(df)
        if remove_outliers:
            df = handle_outliers(df, threshold=z_thresh)

        st.write("### Cleaned Data", df.head())
        st.write(f"Shape: {df.shape}")

        # Download link
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="Download Cleaned CSV",
            data=csv,
            file_name="cleaned_data.csv",
            mime="text/csv",
        )
