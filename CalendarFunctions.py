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

    if isinstance(day, str):
        day = datetime.date.fromisoformat(day)
    
    time_min = datetime.datetime.combine(day, datetime.time.min).isoformat() +"Z"
    time_max = datetime.datetime.combine(day, datetime.time.max).isoformat() +"Z"

    # time_min = datetime.datetime.combine(day, datetime.time.min)
    # time_max = datetime.datetime.combine(day, datetime.time.max)
    

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
        start_dt = datetime.datetime.fromisoformat(start_str)
        start = start_dt.strftime("%H:%M")
        # appointments.append([start, e.get("summary")])
        appointments.append(start)
    return appointments

def create_event(name, email, phone, amount, date, time, difficulty):
    if isinstance(date, str):
        date = datetime.date.fromisoformat(date)
    if isinstance(time, str):
        time = datetime.time.fromisoformat(time)
    
    start_dt = datetime.datetime.combine(date, time)
    end_dt = start_dt + datetime.timedelta(hours=1)

    start = start_dt.isoformat()
    end = end_dt.isoformat()

    event = {
      'summary': f'הזמנה מ{name}, {amount} אנשים, רמת קושי: {difficulty}',
      'location': 'רחוב הדוגמה 1, עיר הדוגמה',
      'description': f'טלפון: {phone}, אימייל: {email}',
      'start': {
        'dateTime': start,
        'timeZone': 'Asia/Jerusalem',
      },
      'end': {
        'dateTime': end,
        'timeZone': 'Asia/Jerusalem',
      },
      'reminders': {
        'useDefault': False,
        'overrides': [
          {'method': 'email', 'minutes': 24 * 60},
          {'method': 'popup', 'minutes': 10},
        ],
      },
    }

    event = service.events().insert(calendarId=calenderID, body=event).execute()
    print('Event created: %s' % (event.get('htmlLink')))
    return event.get('htmlLink')