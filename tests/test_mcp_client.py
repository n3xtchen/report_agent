#! /usr/bin/env python3
# vim:fenc=utf-8
#
# Copyright © 2025 n3xtchen <echenwen@gmail.com>
#
# Distributed under terms of the GPL-2.0 license.

"""

"""

import pytest

from mcp import StdioServerParameters

from report_agent.mcp.client import MCPClient

server_params = StdioServerParameters(
        command="python",
        args=['tests/mcp_server/mcp_test.py'],
        env=None)

@pytest.mark.asyncio
async def test_mcp_tools():
    async with MCPClient(server_params) as client:
        tools = await client.get_available_tools()
        print("xx")
        assert len(tools)>0
