import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Structural Engineering Analysis", layout="wide")

# Custom CSS
with open("static/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Title
st.title("🏗️ Structural Engineering Data Visualization Portal")

# Upload
st.sidebar.header("Upload Data")
uploaded_file = st.sidebar.file_uploader("Upload Excel File", type=["xlsx"])

# Load data
if uploaded_file:
    df = pd.read_excel(uploaded_file)
    df.columns = df.columns.str.strip().str.replace(" ", "_")
    st.subheader("📊 Uploaded Data Preview")
    st.dataframe(df.head())

    # Plot options
    if "Load_kN" in df.columns and "Deflection_mm" in df.columns:
        st.subheader("📈 Load vs Deflection Plot")
        fig, ax = plt.subplots()
        sns.lineplot(data=df, x="Load_kN", y="Deflection_mm", hue="Material_Type", ax=ax)
        st.pyplot(fig)

    if "Stress_MPa" in df.columns and "Strain" in df.columns:
        st.subheader("📈 Stress vs Strain Plot")
        fig, ax = plt.subplots()
        sns.scatterplot(data=df, x="Strain", y="Stress_MPa", hue="Material_Type", ax=ax)
        st.pyplot(fig)

    if "Material_Type" in df.columns:
        st.subheader("🧱 Material-wise Summary")
        st.write(df.groupby("Material_Type").agg(['mean', 'std', 'min', 'max']))

else:
    st.info("Please upload an Excel file with structural data to continue.")
