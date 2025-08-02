import streamlit as st 
import pandas as pd
import numpy as np



# adding the title of your app

st.title("My first app for RAG in Bsic Advance course by Irfan Malik")

# adding simple text

st.write("Hello, World!")

# user input
number = st.slider("Pick a number",0,100)

# print the text of number

st.write("The number is ", number) 

# adding a button

if st.button("Greetings!"):
    st.write("Hi,hello there")
else:
    st.write("GoodBye")
    
# add radio button with options
genre = st.radio(
    "What's your favourite movie genre",
    ("Comedy", "Drama", "Documentary")
)

# print the genre

st.write("your favorite genre:",genre)

# add drop down list

# option = st.selectbox(
#     "How would you like to be contacted?",
#     ("Email", "Home phone", "Mobile phone"))

# add drop down list on left siderbar


option = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone"))

# add your whatsapp number

st.sidebar.text_input("Enter your Whatsapp number")

# add a fileuploader
uploaded_file = st.sidebar.file_uploader("Choose a file", type=["csv", "txt"])

# create a line plot

st.line_chart([1, 2, 3, 4, 5])

# platting
Data = pd.DataFrame({
    'first_col': list(range(1,11)),
    'second_col':np.arange(number,number+10)
})
st.line_chart(Data)