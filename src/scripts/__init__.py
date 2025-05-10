#! /usr/bin/env python3
# vim:fenc=utf-8
#
# Copyright © 2025 n3xtchen <echenwen@gmail.com>
#
# Distributed under terms of the GPL-2.0 license.

"""

"""

from streamlit.web import cli

from views import pandas_agent

def run():
    cli.main_run([pandas_agent.__file__])
