import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My Parents New Healthy Diner')

streamlit.header ('Our BREAKFAST Favourite')
streamlit.text ('🥣 Idli w/ vada curry')
streamlit.text ('Ghee Podi Dosai')
streamlit.text ('Ghee Pongal w/vada')
streamlit.text ('🐔 Kalakki')


streamlit.header('🍌🥭 Build Your Own Fruit Punch 🥝🍇')

my_fruit_list = pandas.read_csv(" https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
#adding a user interface to pick the fruit they want to add
fruits_selected = streamlit.multiselect ("Pick your own choice of fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
#displaying the data in tablular format
streamlit.dataframe(fruits_to_show)



# Create the repeatable code block - function

def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://www.fruityvice.com/api/fruit/" + this_fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized
streamlit.header("Fruityvice Fruit Advice!")
try:
    fruit_choice = streamlit.text_input('What fruit would you like information about?')
    if not fruit_choice:
        streamlit.error("Please select a fruit to get information.")
    else:
        back_from_function = get_fruityvice_data(fruit_choice)
        streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error()



streamlit.header("The Fruit Load list contains:")
#snowflake related functions
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
         my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
         return my_cur.fetchall()

#Add a button to load the fruit
if streamlit.button('Get Fruit Load List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    streamlit.dataframe(my_data_rows)


def insert_row_snowflake(add_my_fruit):
    with my_cnx.cursor() as my_cur:
         my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values ('kiwi')")
         return "Thanks for adding "

add_my_fruit = streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add a fruit to list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_function = insert_row_snowflake(add_my_fruit)
    streamlit.text(back_from_function)

streamlit.stop()
