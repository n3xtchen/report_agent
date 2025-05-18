#! /usr/bin/env python3
# vim:fenc=utf-8
#
# Copyright © 2025 n3xtchen <echenwen@gmail.com>
#
# Distributed under terms of the GPL-2.0 license.

"""
大语言模型管理
"""

from langchain.chat_models import init_chat_model


class LLM:

    @classmethod
    def openai(cls, model: str):

        return init_chat_model(model, model_provider="openai")

    @classmethod
    def claude(cls, model: str):

        return init_chat_model(
            model, 
            model_provider="bedrock_converse",
            credentials_profile_name='bedrock',
            )





