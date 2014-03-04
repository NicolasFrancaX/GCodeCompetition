# -*- coding: utf-8 -*-
# Created on Tue Mar  4 11:05:22 2014
# MIT Licensed. See COPYING.TXT for more information.
""" Turing machine module, for source parsing and simulation """

from __future__ import unicode_literals
import re

__all__ = ["tokenizer"]

def tokenizer(data):
    blocks = []
    for line in data.splitlines():
        if "->" in blocks and "->" in line:
            for token in blocks:
                yield token
            blocks = ["\n"]
            if line[0] == " ":
                blocks.append(" ")
        blocks.extend(re.findall("->|\S+", line))
    for token in blocks:
        yield token
    yield "\n"
