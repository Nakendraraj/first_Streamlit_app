import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header ('Our BREAKFAST Favourite')
streamlit.text ('🥣 Idli w/ vada curry')
streamlit.text ('Ghee Podi Dosai')
streamlit.text ('Ghee Pongal w/vada')
streamlit.text ('🐔 Kalakki')

streamlit.header('🍌🥭 Build Your Own Fruit Punch 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv(" https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
#adding a user interface to pick the fruit they want to add
streamlit.multiselect ("Pick your own choice of fruits:", list(my_fruit_list.index),['Avacado', 'Strawberries'])
#displaying the data in tablular format
streamlit.dataframe(my_fruit_list)
