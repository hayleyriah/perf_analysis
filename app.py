import streamlit as st
import pandas as pd

#load the dataset

df = pd.read_excel("INX_Future_Inc_Employee_Performance_CDS_Project2_Data_V1.8(1) - Copy.xls")

#Add logo

st.image("s-o-c-i-a-l-c-u-t-1RT4txDDAbM-unsplash.jpg")

#provide title for app

st.title("INX Employee Analysis App")

#Add the header

st.header("Dataset Concept.", divider="blue")

#Add paragraph explaining the dataset

st.write("""The dataset gives basic details about employees, 
         like their demographics, job roles, happiness at work, and how 
         well they perform. It's useful for understanding things like why people stay in their jobs, 
         if they're happy, and how they do their work.""")

#-------------------------------------------------------DISPLAY OR EDA----------------------------------------------

st.header("Exploratory Data Analysis (EDA)", divider="rainbow")


#Display more EDA info of the dataset

st.write("Dataset info:",df.info())
st.write("Number of rows in the dataset",df.shape[0]) #[0] <------refers to the rows in the dataset
st.write("Number of columns in the dataset",df.shape[1]) #[1] <-----refers to the columns in the dataset
st.write("Columns Names in the dataset",df.columns.tolist())
st.write("Data types in the dataset",df.dtypes)
st.write("Sum of the missing values in the dataset", df.isnull().sum())
     

# Checkbox to trigger bar chart
bar_chart_checkbox = st.checkbox("Generate Bar Chart")
if bar_chart_checkbox:
    # Plot a bar chart
    selected_columns = st.multiselect("Select the columns to visualize the Bar Chart", df.columns)
    if len(selected_columns) >= 2:
        st.bar_chart(df[selected_columns])
    else:
        st.warning("Please select at least two columns.")

# Checkbox for line chart
line_chart_checkbox = st.checkbox("Generate Line Chart")
if line_chart_checkbox:
    # Plot a line chart
    selected_columns = st.multiselect("Select the columns to visualize the Line Chart", df.columns)
    if len(selected_columns) >= 2:
        st.line_chart(df[selected_columns])
    else:
        st.warning("Please select at least two columns.")

