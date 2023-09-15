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
#adding a user interface to pick the fruit they want to add
streamlit.multiselect ("Pick your own choice of fruit:" list(my_fruits_list.index))
#displaying the data in tablular format
streamlit.dataframe(my_fruit_list)
