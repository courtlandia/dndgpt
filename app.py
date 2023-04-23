import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# Create a sidebar with file upload functionality
st.sidebar.title("Upload CSV")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

# Main page content
st.title("Interactive Plotting with Plotly")
st.write("Upload a CSV file and select columns to visualize.")

# Load data if a file has been uploaded
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Display the raw data table
    st.subheader("Raw Data")
    st.write(df)

    # Allow the user to select columns to visualize
    columns = list(df.columns)
    x_axis = st.selectbox("Select X Axis", columns)
    y_axis = st.selectbox("Select Y Axis", columns)

    # Create a scatter plot using Plotly
    fig = px.scatter(df, x=x_axis, y=y_axis, color="sex")
    st.plotly_chart(fig, use_container_width=True)

if x_axis not in df.columns:
    st.error("Invalid column name for x-axis")
    st.stop()
if y_axis not in df.columns:
    st.error("Invalid column name for y-axis")
    st.stop()
