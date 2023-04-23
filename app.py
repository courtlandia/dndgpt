import streamlit as st
import altair as alt
import pandas as pd

# Set up example data
tips = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv")

# Create chart
chart = alt.Chart(tips).mark_bar().encode(
    x=alt.X('day', title='Day of the week'),
    y=alt.Y('mean(total_bill)', title='Mean total bill'),
    color=alt.Color('sex', title='Sex')
).properties(
    width=alt.Step(40)
)

# Display chart
st.altair_chart(chart, use_container_width=True)

st.balloons()
