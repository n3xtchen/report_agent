#! /usr/bin/env python3
# vim:fenc=utf-8
#
# Copyright © 2025 n3xtchen <echenwen@gmail.com>
#
# Distributed under terms of the GPL-2.0 license.

"""
大语言模型管理
"""

import os

from langchain.chat_models import init_chat_model

DEFAUTL_CLAUDE_MODEL = 'anthropic.claude-3-5-sonnet-20240620-v1:0'
DEFAULT_OPENAI_MODEL = 'gpt-4.1'

class LLMError(Exception):
    """大模型支持情况"""

    def __init__(self, msg: str):
        self.msg = msg

    def __str__(self):
        return f"LLM Error: {self.msg}"


class LLM:

    _llm = None

    @classmethod
    def model(cls):
        """
        - 可选模型：
            - bedrock-claude(默认)
                - 默认模型: claude-3.5
                - 默认配置: bedrock
            - openai
                - 默认模型: gpt-4.1
                - 需要配置 OPENAI_API_KEY
        """

        if cls._llm is not None:
            return cls._llm

        model_provider = os.getenv('LLM_PROVIDER', default='bedrock-claude')
        model_name = os.getenv('LLM_MODEL')
        if model_provider == 'bedrock-claude':
            model_name: str = model_name or DEFAUTL_CLAUDE_MODEL
            cls._llm = cls.claude(model_name)
        elif model_provider == 'openai':
            model_name = model_name or DEFAUTL_OPENAI_MODEL
            # if os.getenv('OPENAI_API_KEY', None) is None:
            #     return 'error'
            cls._llm = cls.openai(model_name)
        else:
            raise LLMError(f"Provider {model_provider} is Not Support!")

        return cls._llm

    @classmethod
    def openai(cls, model: str):

        return init_chat_model(model, model_provider="openai")

    @classmethod
    def claude(cls, model: str, profile_name: str='bedrock'):

        return init_chat_model(
            model, 
            model_provider="bedrock",
            credentials_profile_name=profile_name
            )

