import streamlit as st
import pandas as pd

st.set_page_config(page_title="Cloud File Analyzer", layout="centered")

st.title("☁️ Cloud File Analyzer")
st.write("Upload a file and analyze it instantly")

# File upload
uploaded_file = st.file_uploader("Upload a CSV or TXT file", type=["csv", "txt"])

if uploaded_file is not None:
    file_type = uploaded_file.name.split(".")[-1]

    st.success("File uploaded successfully!")

    # CSV handling
    if file_type == "csv":
        df = pd.read_csv(uploaded_file)

        st.subheader("📊 Data Preview")
        st.dataframe(df.head())

        st.subheader("📈 Basic Statistics")
        st.write(df.describe())

    # TXT handling
    elif file_type == "txt":
        text = uploaded_file.read().decode("utf-8")

        st.subheader("📄 File Content")
        st.text(text[:500])

        st.subheader("🔢 Text Analysis")
        st.write("Character count:", len(text))
        st.write("Word count:", len(text.split()))

else:
    st.warning("Please upload a file to proceed.")