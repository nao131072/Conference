"""
Manage the link to the Google Meet API
"""

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.apps import meet_v2
from env_util.env_manager import EnvManager
import json

class Api():
    SCOPES = ['https://www.googleapis.com/auth/meetings.space.created']

    def __init__(self):
        pass

    @classmethod
    def user_access_app(cls, user_token = None) -> str:
        """
        Try to access app through the Google Meet API
        """
        user_creds = None
        
        # Read user token
        if user_token is not None:
            user_creds = Credentials.from_authorized_user_info(user_token, Api.SCOPES)

        if not user_creds or not user_creds.valid:
            # token expired, refresh it
            if user_creds and user_creds.expired and user_creds.refresh_token:
                user_creds.refresh(Request())
            # no token create one
            else:
                credpath = EnvManager.credentials
                flow = InstalledAppFlow.from_client_secrets_file(
                    credpath, Api.SCOPES)
                user_creds = flow.run_local_server(port=0)
            
            new_token = user_creds.to_json()
            return new_token
        
        return None

    @classmethod
    def create_meeting(cls, user_token: str|dict):
        """
        Create a meeting
        """
        if isinstance(user_token, str):
            user_token = json.loads(user_token)
        user_cred = Credentials.from_authorized_user_info(user_token, Api.SCOPES)
        try:
            client = meet_v2.SpacesServiceClient(credentials=user_cred)
            request = meet_v2.CreateSpaceRequest()
            space = request.space
            space.config.access_type = meet_v2.SpaceConfig.AccessType.OPEN
            response = client.create_space(request=request)
            print(f'Space created: {response.meeting_uri}')
        except Exception as error:
            # TODO(developer) - Handle errors from Meet API.
            print(f'An error occurred: {error}')

if __name__ == '__main__':
    import json

    new_token:str = Api.user_access_app()
    Api.create_meeting(new_token)
    