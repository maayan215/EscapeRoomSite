import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/calendar"]

# Refer to the Python quickstart on how to setup the environment:
# https://developers.google.com/workspace/calendar/quickstart/python
# Change the scope to 'https://www.googleapis.com/auth/calendar' and delete any
# stored credentials.

calenderID = "98e7e029e0db38364acae09e909908bbf9eb916b502db328b4148147d8e41687@group.calendar.google.com"
creds = Credentials.from_authorized_user_file("token.json", SCOPES)
service = build("calendar", "v3", credentials=creds)
now = datetime.datetime.now(tz=datetime.timezone.utc).isoformat()

event_result = service.events().list(
   calendarId=calenderID,
).execute()
events = event_result.get("items", [])
#for event in events:
#    start = event["start"].get("dateTime", event["start"].get("date"))
#    print(start, event["summary"])
# print(event_result.get("items", []))
def get_open_on_Day(day):
    time_min = datetime.datetime.combine(day, datetime.time.min).isoformat() + "Z"
    time_max = datetime.datetime.combine(day, datetime.time.max).isoformat() + "Z"
   
    events_result = service.events().list(
        calendarId=calenderID,   # or your calendar ID
        timeMin=time_min,
        timeMax=time_max,
        singleEvents=True,
        orderBy="startTime"
    ).execute()

    events = events_result.get("items", [])
    appointments = []
    for e in events:
        start_str = e["start"].get("dateTime", e["start"].get("date"))
        start_dt = datetime.fromisoformat(start_str.replace("Z", "+00:00"))
        start = start_dt.strftime("%H:%M")
        appointments.append([start, e.get("summary")])
    return appointments
day = datetime.date(2025, 9, 23)
print(get_open_on_Day(day))