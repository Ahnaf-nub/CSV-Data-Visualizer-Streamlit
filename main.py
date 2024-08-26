import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Interactive Data Visualization Tool with AI-Powered Insights")
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
                                      "Line Plot", 
                                      "Bar Plot", 
                                      "Histogram", 
                                      "Pair Plot",
                                      "Time Series",
                                      "Box Plot",
                                      "Violin Plot",
                                      "Correlation Matrix",
                                      "Data Summary"])

    # Select columns for x and y axes
    if plot_type not in ["Histogram", "Pie Chart", "Heatmap", "Pair Plot", "Correlation Matrix", "Data Summary"]:
        x_column = st.sidebar.selectbox("Select X-axis", df.columns)
        y_column = st.sidebar.selectbox("Select Y-axis", df.columns)
    
    # Scatter Plot
    if plot_type == "Scatter Plot":
        st.write(f"Scatter Plot of {x_column} vs {y_column}")
        plt.figure(figsize=(8, 6))
        sns.scatterplot(x=df[x_column], y=df[y_column])
        st.pyplot(plt)

    # Line Plot
    elif plot_type == "Line Plot":
        st.write(f"Line Plot of {x_column} vs {y_column}")
        plt.figure(figsize=(8, 6))
        sns.lineplot(x=df[x_column], y=df[y_column])
        st.pyplot(plt)

    # Bar Plot
    elif plot_type == "Bar Plot":
        st.write(f"Bar Plot of {x_column} vs {y_column}")
        plt.figure(figsize=(8, 6))
        sns.barplot(x=df[x_column], y=df[y_column])
        st.pyplot(plt)

    # Histogram
    elif plot_type == "Histogram":
        st.write(f"Histogram of {x_column}")
        plt.figure(figsize=(8, 6))
        sns.histplot(df[x_column], kde=True, bins=30)
        st.pyplot(plt)

    # Pair Plot
    elif plot_type == "Pair Plot":
        st.write("Pair Plot of Selected Columns")
        sns.pairplot(df)
        st.pyplot()
        
    # Box Plot
    elif plot_type == "Box Plot":
        st.write(f"Box Plot of {y_column} grouped by {x_column}")
        plt.figure(figsize=(8, 6))
        sns.boxplot(x=df[x_column], y=df[y_column])
        st.pyplot(plt)

    # Violin Plot
    elif plot_type == "Violin Plot":
        st.write(f"Violin Plot of {y_column} grouped by {x_column}")
        plt.figure(figsize=(8, 6))
        sns.violinplot(x=df[x_column], y=df[y_column])
        st.pyplot(plt)

    # Time Series
    elif plot_type == "Time Series":
        if pd.api.types.is_datetime64_any_dtype(df[x_column]) or pd.api.types.is_numeric_dtype(df[x_column]):
            st.write(f"Time Series Plot of {y_column} over {x_column}")
            plt.figure(figsize=(10, 6))
            sns.lineplot(x=df[x_column], y=df[y_column])
            st.pyplot(plt)
        else:
            st.write(f"Please select a datetime or numeric column for the X-axis to plot a time series.")

    # Correlation Matrix
    elif plot_type == "Correlation Matrix":
        st.write("Correlation Matrix")
        corr = df.corr()
        st.write(corr)
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr, annot=True, cmap="coolwarm", linewidths=0.5)
        st.pyplot(plt)

    # Data Summary
    elif plot_type == "Data Summary":
        st.write("Summary Statistics")
        st.write(df.describe().T)
        st.write("Missing Values")
        st.write(df.isnull().sum())
else:
    st.write("Please upload a CSV file to begin.")
