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


# New section to pull fruity vice api response
streamlit.header("Fruityvice Fruit Advice!")

# new entries for nested if else

fruit_choice = streamlit.text_input('What fruit would you like information about?')
if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
else:
    fruityvice_response = requests.get("https://www.fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    streamlit.dataframe(fruityvice_normalized)
    
except URLError as e:
  streamlit.error()

streamlit.stop()



my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.text("The Fruit Load list contains:")
streamlit.dataframe(my_data_rows)
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice1 = streamlit.text_input('What fruit would you like information about?', 'jackfruit')

my_cur.execute("insert into fruit_load_list values ('from streamlit')")
