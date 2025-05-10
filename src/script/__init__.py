#! /usr/bin/env python3
# vim:fenc=utf-8
#
# Copyright © 2025 n3xtchen <echenwen@gmail.com>
#
# Distributed under terms of the GPL-2.0 license.

"""

"""

from script import pandas_agent
from streamlit.web import cli

def run():
    print(pandas_agent.__file__)
    cli.main_run([pandas_agent.__file__])
