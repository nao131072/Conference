"""
Manages the private data.
"""

import os.path

class EnvManager:
    abs = os.path.abspath(os.path.dirname(__file__)) + "/"


    credentials = abs + r"env/credentials.json"
    token = abs + r"env/token.json"