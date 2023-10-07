from sqlalchemy import create_engine
import streamlit as st
import pandas as pd
import os
import json
from dotenv import load_dotenv
import datetime

load_dotenv()

sf_username = os.environ.get("SNOWFLAKE_USERNAME")
sf_password = os.environ.get("SNOWFLAKE_PASSWORD")
sf_account_identifier = os.environ.get("SNOWFLAKE_ACCOUNT_IDENTIFIER")
sf_db = os.environ.get("SNOWFLAKE_DB")
sf_schema = os.environ.get("SNOWFLAKE_SCHEMA")
connection_string = f'snowflake://{sf_username}:{sf_password}@{sf_account_identifier}/{sf_db}/{sf_schema}'

engine = create_engine(connection_string)

connection = engine.connect()   
try:
    # Streamlit app header
    st.title('Samsung Marketing Insights Dashboard')

    st.sidebar.title("Adjust Parameters")

    data = {}
    with open("streamlit/sql.json") as f:
        data = json.load(f)    
    
    names_queries = {i["name"]: {"query": i["query"], "variables": i["variables"]} for i in data["data"]}

    option = st.sidebar.selectbox('queries', names_queries.keys())


    selected_query = names_queries[option]["query"]

    variables_list = []
    err = 0
    for var in names_queries[option]["variables"]:
        if var["type"] == "dropdown":
            var_value = st.sidebar.selectbox(label=var["name"], options= var["values"])
        elif var["type"] == "int":
            try:
                var_value = int(st.sidebar.text_input(label=var["name"], value=0))
            except ValueError:
                st.sidebar.write(':red[Please enter a number!]')
                err += 1
                continue
           # if var["name"] == 'Manufacturer ID' and var_value < 3 :
            #     st.sidebar.write("Only enter 3 digits")

            
        elif var["type"] == "string":
            try:
                var_value = st.sidebar.text_input(label=var["name"], value='')
            except ValueError:
                st.sidebar.write(':red[Enter a proper value]')
                err += 1
        elif var["type"] == "date":
            var_value = str(st.sidebar.date_input(var["name"], value = datetime.date(2000,1,1), format = "YYYY-MM-DD"))
        else:
            raise(ValueError("Unknown param"))

        variables_list.append(var_value)

    if err == 0 and st.sidebar.button('Run'):
        new_selected_query = selected_query.format(*variables_list)

        with engine.connect() as connection:
            # try:
            result = connection.execute(new_selected_query)
            df = pd.DataFrame(result.fetchall(), columns=result.keys())
            st.dataframe(df)
            # except:
            #     st.write("Unexpected Error! - Please check the input")


           # if option == "Store & Web Sales Quarterly Increment":
           #      st.write("Store & Web Sales Quarterly Increment Data")   
           #      st.bar_chart(df)
           # elif option == "Manufacturer Sales Analysis":
           #      st.write("Manufacturer Sales Analysis Data")
                 
         

    
finally:
    connection.close()
    engine.dispose()

