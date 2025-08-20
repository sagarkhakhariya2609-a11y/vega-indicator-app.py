import streamlit as st
import pandas as pd

st.title("Vega Indicator App")

uploaded_file = st.file_uploader("Upload Option Chain CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df.head())

    if "Vega" in df.columns:
        df["Signal"] = df["Vega"].apply(lambda x: "Positive" if x > 0 else "Negative")
        st.write("Processed Data with Vega Signal:")
        st.dataframe(df)
    else:
        st.error("CSV file must contain a 'Vega' column.")
