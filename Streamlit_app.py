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
fruits_selected = streamlit.multiselect ("Pick your own choice of fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
#displaying the data in tablular format
streamlit.dataframe(fruits_to_show)

# New section to pull fruity vice api response
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://www.fruityvice.com/api/fruit/" + "kiwi")

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)
