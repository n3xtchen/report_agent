#! /usr/bin/env python3
# vim:fenc=utf-8
#
# Copyright © 2025 n3xtchen <echenwen@gmail.com>
#
# Distributed under terms of the GPL-2.0 license.

"""

"""

import asyncio
import streamlit as st
from langchain_mcp_adapters.client import MultiServerMCPClient

async def chat_ui(client, tools, selected_model):
    st.title("LLM Assistant with MCP Tools")
    st.write("Enter your query below to interact with the LLM and MCP tools.")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    user_input = st.chat_input("Enter your prompt")
    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})

        with st.chat_message("user"):
            st.markdown(user_input)

        # if client:
        #     # response, messages = await agent_loop(user_input, tools, client, st.session_state.messages, selected_model)
        #     st.session_state.messages = messages

        with st.chat_message("assistant"):
            st.markdown('Pong')

def sidebar():
    with st.sidebar:
        st.title("Configuration")

        # Available Tools
        st.subheader("Available Tools")
        print(st.session_state)
        if "tools" in st.session_state:
            with st.expander("Tool List", expanded=False):
                for tool_name, tool_details in st.session_state.tools.items():
                    st.markdown(f"- *{tool_name}*: {tool_details['schema']['function']['description']}")
        else:
            st.write("Tools loading... Please wait.")


        # API Configuration
        st.subheader("API Configuration")

    return None, None


async def main():
    st.set_page_config(layout="wide")

    client, selected_model = sidebar()

    async with MultiServerMCPClient({
        "weather": {
            "command": "python",
            "args": ["src/mcp-stdio-get-weather.py"],
            "transport": "stdio"
        }
    }) as client:

        tools = {
            tool.name: {
                "name": tool.name,
                "callable": None,
                "schema": {
                    "type": "function",
                    "function": {
                        "name": tool.name,
                        "description": tool.description,
                        "parameters": []
                    },
                },
            }
            for tool in client.get_tools()
        }
        st.session_state.tools = tools
        print(st.session_state)

        await chat_ui(client, tools, selected_model)

if __name__ == '__main__':
    asyncio.run(main())
