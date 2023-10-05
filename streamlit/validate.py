from snowflake.sqlalchemy import URL
from sqlalchemy import create_engine
import urllib.parse
import streamlit as st
import pandas as pd
import numpy as np
import json
import re



quoted_password = urllib.parse.quote("Hellrock@079")

url = f'snowflake://ajaiswal95:{quoted_password}@qefqbdp-ryb09972/SNOWFLAKE_SAMPLE_DATA/TPCDS_SF10TCL?COMPUTE_WH&ACCOUNTADMIN'

engine = create_engine(url)

engine = create_engine(URL(
        user='ajaiswal95',
        password=quoted_password,
        account='qefqbdp-ryb09972',
        database = 'SNOWFLAKE_SAMPLE_DATA',
        schema = 'TPCDS_SF10TCL',
        warehouse = 'COMPUTE_WH',
        role = 'ACCOUNTADMIN',
    )
)
connection = engine.connect()   
try:
    # Streamlit app header
    st.title('Interactive Snowflake Query Runner')

    data = {}
    with open("./sql.json") as f:
        data = json.load(f)    

    names_queries = {i["name"]: {"query":i["query"], "variables":i["variables"]} for i in data["data"]}

    option = st.selectbox('queries', names_queries.keys())

    # st.write(names_queries[option])

    selected_query = names_queries[option]["query"]

    variables_list = []
    for var in names_queries[option]["variables"]:
        if var["type"] == "dropdown":
            var_value = st.selectbox(label=var["name"], options= var["values"])
        elif var["type"] == "int":
                try:
                    var_value = int(st.text_input(label=var["name"], value=0))
                except ValueError:
                    print('Please enter a number!')
        elif var["type"] == "string":
                var_value = st.text_input(label=var["name"], value='')
        else:
                raise(ValueError(""))
        variables_list.append(var_value)

    st.write(variables_list)

   # button1 = st.button('Show Query')
   # if st.session_state.get('button') != True:
    #    st.session_state['button'] = button1
    if st.button('Run'):
            new_selected_query = selected_query.format(*variables_list)
         #   colored_selected_query = re.sub(r'\{(\d+)\}', r':blue[{\1}]', selected_query)
          #  st.write(colored_selected_query.format(*variables_list))
        
            with engine.connect() as connection:
                result = connection.execute(new_selected_query)
                df = pd.DataFrame(result.fetchall(), columns=result.keys())
                st.dataframe(df)
                
    
            if option == "Store & Web Sales Quarterly Increment":
                 st.write('AJ')
                 st.bar_chart(df)
        


    
    
finally:
    connection.close()
    engine.dispose()

