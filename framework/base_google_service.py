import os
import pickle

from google.auth.transport._http_client import Request
from google_auth_oauthlib.flow import InstalledAppFlow

from utils.environmnets import env


class BaseService(object):
    """
    Responsible for basic operations with Google service api
    """
    def __init__(self):
        self.creds = self.auth_to_google_api()
        self.service = None

    @staticmethod
    def auth_to_google_api():
        """
        Authorize to Google service.
        You need to place values under variables "PATH_TO_TOKEN_FOLDER", "PATH_TO_CREDS_FILE", "SCOPES" in order to
        be able to use them for authorization and authentication
        :return: credentials needed for service
        """
        creds = None
        if os.path.exists(f'{env("PATH_TO_TOKEN_FOLDER")}token.pickle'):
            with open(f'{env("PATH_TO_TOKEN_FOLDER")}token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    # If modifying these SCOPES, delete the file token.pickle.
                    env('PATH_TO_CREDS_FILE'), env('SCOPES'))
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(f'{env("PATH_TO_TOKEN_FOLDER")}token.pickle', 'wb') as token:
                pickle.dump(creds, token)
        return creds
