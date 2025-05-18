#! /usr/bin/env python3
# vim:fenc=utf-8
#
# Copyright © 2025 n3xtchen <echenwen@gmail.com>
#
# Distributed under terms of the GPL-2.0 license.

"""
测试模型
"""

import pytest

from report_agent.chat_model import LLM

@pytest.mark.asyncio
async def test_bedrock_converse():

    model_name="anthropic.claude-3-5-sonnet-20240620-v1:0"

    model = LLM.claude(model_name)
    response = model.invoke("Hello, world!")
    assert response is not None

@pytest.mark.asyncio
async def test_openai():

    model = LLM.openai("gpt-4.1")
    response = model.invoke("Hello, world!")
    assert response is not None

