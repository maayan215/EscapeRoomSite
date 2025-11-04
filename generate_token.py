import os
import json
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials

SCOPES = ["https://www.googleapis.com/auth/calendar"]

CLIENT_ID = "282890865336-2kqpb54vnnpf1ssiku1q76gi603mhjnm.apps.googleusercontent.com"
CLIENT_SECRET = "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"
REDIRECT_URI = "http://localhost:8080/oauth2callback"

def main():
    flow = InstalledAppFlow.from_client_config(
        {
            "web": {
                "client_id": CLIENT_ID,
                "client_secret": CLIENT_SECRET,
                "redirect_uris": [REDIRECT_URI],
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token"
            }
        },
        SCOPES
    )

    creds = flow.run_local_server(port=8080)
    token = creds.to_json()

    print("\n✅ COPY THIS VALUE AND PASTE INTO RENDER AS GOOGLE_CREDENTIALS:\n")
    print(token)
    print("\n✅ Done.\n")


if __name__ == "__main__":
    main()
