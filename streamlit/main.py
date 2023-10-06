import streamlit as st
from streamlit_extras.stateful_button import button
import json
from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv
import os
import re

load_dotenv()

st.title("Assignment 1")

sf_username = os.environ.get("SNOWFLAKE_USERNAME")
sf_password = os.environ.get("SNOWFLAKE_PASSWORD")
sf_account_identifier = os.environ.get("SNOWFLAKE_ACCOUNT_IDENTIFIER")
sf_db = os.environ.get("SNOWFLAKE_DB")
sf_schema = os.environ.get("SNOWFLAKE_SCHEMA")
connection_string = f'snowflake://{sf_username}:{sf_password}@{sf_account_identifier}/{sf_db}/{sf_schema}'

engine = create_engine(connection_string)

data = {}
with open("./queries.json") as f:
    data = json.load(f)

names_queries = {i["name"]: (i["query"], i["variables"]) for i in data["data"]}

option = st.selectbox('queries', names_queries.keys())

selected_query = names_queries[option][0]

variables_list = []
for k, v in names_queries.items():
    if k == option:
        if len(v[1]) == 0:
            st.write("No variables!")
        for i in range(len(v[1])):
            if v[1][i]["type"] == "dropdown":
                var_value = st.selectbox(label=v[1][i]["name"], options= v[1][i]["values"])
            elif v[1][i]["type"] == "int":
                # TODO: error handling, what if string is passed - done
                # TODO: put bounds to numbers
                try:
                    var_value = int(st.text_input(label=v[1][i]["name"], value=0))
                except ValueError:
                    print('Please enter a number!')
            elif v[1][i]["type"] == "string":
                var_value = st.text_input(label=v[1][i]["name"], value='')
            else:
                raise(ValueError(""))
            variables_list.append(var_value)

if button("Show Query", key = "Show Query"):
    new_selected_query = selected_query.format(*variables_list)
    colored_selected_query = re.sub(r'\{(\d+)\}', r':blue[{\1}]', selected_query)
    st.write(colored_selected_query.format(*variables_list))
    if button("Run", key = "Run"):
        with engine.connect() as connection:
            result = connection.execute(new_selected_query)
            df = pd.DataFrame(result.fetchall(), columns=result.keys())
            st.dataframe(df)



