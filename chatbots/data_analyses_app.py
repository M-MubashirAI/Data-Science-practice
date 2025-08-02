import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 


# adding the title of your apps

st.title("Data Ananlyses Application")
st.subheader("This is the simple data Analysis App and created by Mubashir Malik")

# create a dropdown list to choose a dataset

dataset_list = ["iris","tips","titanic","diamonds"]

dataset = st.selectbox("Select Dataset",dataset_list)

# load the selected dataset
if dataset == "iris":
    df = sns.load_dataset("iris")

elif dataset == "tips":
    df = sns.load_dataset("tips")

elif dataset == "titanic":
    df = sns.load_dataset("titanic")

elif dataset == "diamonds":
    df = sns.load_dataset("diamonds")
    
# button to uppload custom dataset
upload_file = st.file_uploader("Upload a custum dataset",type=["csv","xlsx"])

if upload_file is not None:
    df = pd.read_csv(upload_file)

st.write(df)

# display the dataset
st.write(df)

# display the number Rows and Columns from dataset

st.write("The Number of Rows",df.shape[0])

st.write("The Number of Columns",df.shape[1])

# Display the column name of dataset with their data types

st.write("The Column Name and data Types:",df.dtypes)

# display the null values

if df.isnull().sum().sum() > 0:
    st.write("The Null Values in the dataset are: ",df.isnull().sum().sort_values(ascending=False))

else:
    st.write("There are no null values in the dataset")
    
# display the summary of statistics 

st.write("Summary Statistics:",df.describe())

# Select specific columns for X and Y axis from the dataset and also select plot type to plot the data

x_axis = st.selectbox("Select X axis",df.columns)
y_axis = st.selectbox("Select Y axis",df.columns)
plot_type = st.selectbox("Select Plot Type",["scatter","line","bar","box","hist","kde"])

# plot the data
if plot_type == "scatter":
    st.scatter_chart(df[[x_axis,y_axis]])
elif plot_type == "line":
    st.line_chart(df[[x_axis,y_axis]])
elif plot_type == "bar":
    st.bar_chart(df[[x_axis,y_axis]])
elif plot_type == "box":
    df[[x_axis,y_axis]].plot(kind="box")
    st.pyplot()
elif plot_type == "hist":
    df[x_axis].plot(kind="hist")
    st.pyplot()
elif plot_type == "kde":
    df[[x_axis,y_axis]].plot(kind="kde")
    
    

