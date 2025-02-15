"""
Manages the private data.
"""

import os.path

class EnvManager:
    abs = os.path.abspath(os.path.dirname(__file__)) + "/"
    credentials = abs + r"env/credentials.json"
    token_path = abs + r"env/token.json"

if __name__ == "__main__":
    print(EnvManager.credentials)