"""
Manages the private data.
"""

import os.path

class EnvManager:
    abs = os.path.abspath(os.path.dirname(__file__)) + "/"


    credentials = abs + r"env/credentials.json"
    token_folder = abs + r"env/tokens/"

    @classmethod
    def save_user_token(cls, user_id: int, token: str) -> None:
        """
        Save the user token
        """
        # make user id 1 to 0001
        if token is None:
            return
        user_id = str(user_id).zfill(4)
        file_name = cls.token_folder + user_id + ".json"
        with open(file_name, 'w') as f:
            f.write(token)
    
    @classmethod
    def find_user_token(cls, user_id: int) -> str:
        """
        Find the user token
        """
        user_id = str(user_id).zfill(4)
        file_name = cls.token_folder + user_id + ".json"
        if os.path.isfile(file_name):
            with open(file_name, 'r') as f:
                data = f.read()
                if data:
                    return data
        return None