import streamlit as st
import json

st.title("Assignment 1")

data = {}
with open("./queries.json") as f:
    data = json.load(f)

names_queries = {i["name"]: (i["query"], i["variables"]) for i in data["data"]}

option = st.selectbox('queries', names_queries.keys())

selected_query = names_queries[option][0]

variables_list = []
for k, v in names_queries.items():
    if k == option:
        for i in range(len(v[1])):
            # v[1] is list of variables
            # i = 2 here, each v[1][i] is a dict
            # if v[1][i]["type"] is dropdown, put dropdown
            # else if v[1][i]["type"] is int, put input_text
            if v[1][i]["type"] == "dropdown":
                var_value = st.selectbox(label=v[1][i]["name"], options= v[1][i]["values"])
            elif v[1][i]["type"] == "int":
                # TODO: error handling, what if string is passed
                var_value = int(st.text_input(label=v[1][i]["name"], value=0))
            elif v[1][i]["type"] == "string":
                var_value = st.text_input(label=v[1][i]["name"], value='')
            else:
                raise(ValueError(""))
            variables_list.append(var_value)

if st.button('Submit'):
    new_selected_query = selected_query.format(*variables_list)
    st.write(new_selected_query)





