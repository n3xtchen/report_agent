#! /usr/bin/env python3
# vim:fenc=utf-8
#
# Copyright © 2025 n3xtchen <echenwen@gmail.com>
#
# Distributed under terms of the GPL-2.0 license.

"""
"""



from langchain.sql_database import SQLDatabase
from langchain.agents import AgentType
from langchain.callbacks import StreamlitCallbackHandler
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
import streamlit as st

from report_agent.chat_model import LLM


st.title("Talk to your data")
db_string = st.text_input("db_string")

# 如果使用 bedrock, 不能用 bedrock_converse 
# todo: 在这里加一个验证不是 bedrock_converse
llm = LLM.model()

if db_string:
    db = SQLDatabase.from_uri(db_string)
    toolkit = SQLDatabaseToolkit(db=db, llm=llm)
    agent_executor = create_sql_agent(
        llm=llm,
        toolkit=toolkit,
        verbose=True,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    )
    
    if prompt := st.chat_input():
        st.chat_message("user").write(prompt)
        with st.chat_message("assistant"):
            st_callback = StreamlitCallbackHandler(st.container())
            response = agent_executor.run(prompt, callbacks=[st_callback])
    
            st.write(response)

