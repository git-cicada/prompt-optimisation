# %load -r 3:25 _init.py
import pathlib
import sammo
from sammo.runners import OpenAIChat
from sammo.base import Template, EvaluationScore
from sammo.components import Output, GenerateText, ForEach, Union
from sammo.extractors import ExtractRegex
from sammo.data import DataTable
import json
import requests
import os

_ = sammo.setup_logger("WARNING")  # we're only interested in warnings for now

# Create SAMMO-compatible runner for LM Studio
runner = OpenAIChat(
    model="llama-3.2-3b-instruct",  # or any model you've loaded in LM Studio
    base_url="http://localhost:1234/v1",  # LM Studio endpoint
    api_key="lm-studio"  # dummy key
)

spp_hello_world = Output(GenerateText("Hello World!"))
spp_hello_world.run(runner)

"""
SAMMO CURRENLTY NOT SUPPORTING LM STUDIO
"""