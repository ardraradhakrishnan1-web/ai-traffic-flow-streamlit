import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# App title
st.title("AI-Based Traffic Flow Analysis")

# Load dataset
df = pd.read_csv("traffic.csv")

# Check columns
st.subheader("Dataset Columns")
st.write(df.columns)

# Convert DateTime column
df['DateTime'] = pd.to_datetime(df['DateTime'])

# Dataset preview
st.subheader("Dataset Preview")
st.dataframe(df.head())

# KPI cards
col1, col2 = st.columns(2)
col1.metric("Average Traffic Volume", round(df['Vehicles'].mean(), 2))
col2.metric("Total Records", len(df))

# Junction filter
junction = st.selectbox("Select Junction", df['Junction'].unique())
filtered_df = df[df['Junction'] == junction]

# Line chart
st.subheader("Traffic Flow Over Time")
fig, ax = plt.subplots()
ax.plot(filtered_df['DateTime'], filtered_df['Vehicles'])
ax.set_xlabel("Date")
ax.set_ylabel("Vehicles")
st.pyplot(fig)

# Bar chart
st.subheader("Traffic Volume by Junction")
junction_data = df.groupby("Junction")["Vehicles"].sum()

fig2, ax2 = plt.subplots()
junction_data.plot(kind="bar", ax=ax2)
ax2.set_xlabel("Junction")
ax2.set_ylabel("Total Vehicles")
st.pyplot(fig2)
