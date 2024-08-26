import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Interactive Data Visualization Tool")
st.write("Upload your dataset to explore and visualize the data.")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    df = df.fillna(0)  # Replace missing values with 0 or any other appropriate value
    st.write("Dataset Preview:")
    st.write(df.head())

    # Convert categorical columns to numeric using one-hot encoding
    df = pd.get_dummies(df, drop_first=True)

    st.write("Processed Dataset Preview (after encoding):")
    st.write(df.head())

    st.sidebar.header("Visualization Settings")

    # Select the type of plot
    plot_type = st.sidebar.selectbox("Choose plot type", 
                                     ["Scatter Plot", 
                                      "Line Plot", ])

    # Select columns for x and y axes
    x_column = st.sidebar.selectbox("Select X-axis", df.columns)
    y_column = st.sidebar.selectbox("Select Y-axis", df.columns)

    if plot_type == "Scatter Plot":
        st.write(f"Scatter Plot of {x_column} vs {y_column}")
        plt.figure(figsize=(8, 6))
        sns.scatterplot(x=df[x_column], y=df[y_column])
        st.pyplot(plt)

    elif plot_type == "Line Plot":
        st.write(f"Line Plot of {x_column} vs {y_column}")
        plt.figure(figsize=(8, 6))
        sns.lineplot(x=df[x_column], y=df[y_column])
        st.pyplot(plt)
else:
    st.write("Please upload a CSV file to begin.")
