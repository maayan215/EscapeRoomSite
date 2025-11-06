
import datetime
# import os.path
from datetime import timedelta, date, time
import json
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import dateutil.parser
import os
import urllib.parse
# from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
# from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/calendar"]

# Refer to the Python quickstart on how to setup the environment:
# https://developers.google.com/workspace/calendar/quickstart/python
# Change the scope to 'https://www.googleapis.com/auth/calendar' and delete any
# stored credentials.

def get_google_credentials():
    """Load credentials JSON from env, ensure scope, auto-refresh if needed."""
    # creds_json = os.getenv("token.json")
    # if not creds_json:
    #     raise ValueError("Google credentials not found in environment variables.")
    # creds_dict = json.loads(creds_json)

    with open("token.json", "r", encoding="utf-8") as f:
        creds_dict = json.load(f)

    # IMPORTANT: ensure scope is applied
    creds = Credentials.from_authorized_user_info(creds_dict, SCOPES)

    # Auto-refresh if expired (requires refresh_token in creds)
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
        # Write back the refreshed token so subsequent calls use it (temporary in-memory)
        os.environ["credentials"] = creds.to_json()

    return creds

def get_service():
    """Build a Calendar API service using current credentials."""
    creds = get_google_credentials()
    return build("calendar", "v3", credentials=creds)

calenderID = "98e7e029e0db38364acae09e909908bbf9eb916b502db328b4148147d8e41687@group.calendar.google.com"
# creds = Credentials.from_authorized_user_file("token.json", SCOPES)
# ❌ removed global service + now-at-import usage to avoid deploy crashes

def get_open_on_Day(day):

    if isinstance(day, str):
        day = datetime.date.fromisoformat(day)
    
    time_min = datetime.datetime.combine(day, datetime.time.min).isoformat() +"Z"
    time_max = datetime.datetime.combine(day, datetime.time.max).isoformat() +"Z"

    service = get_service()
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
        if e.get("summary") == "תור פנוי":
            appointments.append(start)
    print(events)
    return appointments

def get_Specific_Event(date_value, time_value):
    """ date_value: date object or 'YYYY-MM-DD' string
        time_value: time object or 'HH:MM' string
    """
    if isinstance(date_value, str):
        date_value = date.fromisoformat(date_value)
    if isinstance(time_value, str):
        time_value = time.fromisoformat(time_value)

    # Make sure all times are timezone-aware (UTC)
    start_of_day = datetime.datetime.combine(date_value, datetime.datetime.min.time(), tzinfo=datetime.timezone.utc)
    end_of_day = datetime.datetime.combine(date_value, datetime.datetime.max.time(), tzinfo=datetime.timezone.utc)

    service = get_service()
    events_result = service.events().list(
        calendarId=calenderID,
        timeMin=start_of_day.isoformat(),
        timeMax=end_of_day.isoformat(),
        singleEvents=True,
        orderBy="startTime"
    ).execute()

    events = events_result.get("items", [])
    if not events:
        # print('No events found on this day.')
        return None
    # print(f'Found {len(events)} events on this day.')
    target_dt = datetime.datetime.combine(date_value, time_value).replace(tzinfo=datetime.timezone.utc)

    for event in events:
        start = event["start"].get("dateTime")
        end = event["end"].get("dateTime")
        if not (start and end):
            continue

        start_dt = datetime.datetime.fromisoformat(start)
        end_dt = datetime.datetime.fromisoformat(end)
        start_dt = start_dt.replace(tzinfo=datetime.timezone.utc)
        end_dt = end_dt.replace(tzinfo=datetime.timezone.utc)
        # print(f'Checking event from {start_dt} to {end_dt} with target {target_dt}')
        if start_dt <= target_dt < end_dt:
            return event

    return None

def create_event(name, email, phone, amount, date, time, difficulty):
  
    holder = get_Specific_Event(date, time)
    service = get_service()
    service.events().delete(calendarId=calenderID, eventId=holder['id']).execute()

    if isinstance(date, str):
        date = datetime.date.fromisoformat(date)
    if isinstance(time, str):
        time = datetime.time.fromisoformat(time).replace(tzinfo=datetime.timezone.utc)
     
    start_dt = datetime.datetime.combine(date, time) - timedelta(hours=3)
    end_dt = start_dt + datetime.timedelta(hours=1.5)

    # start_dt = start_dt.replace(tzinfo=datetime)
    # end_dt = end_dt.replace(tzinfo=datetime.timezone.utc)


    # start_dt = datetime.datetime.combine(start_dt, datetime.datetime.min.time(), tzinfo=datetime.timezone.utc)
    # end_dt = datetime.datetime.combine(end_dt, datetime.datetime.max.time(), tzinfo=datetime.timezone.utc)


    # start = start_dt.isoformat() + 'Z'
    # end = end_dt.isoformat() + 'Z'

    event = {
      'summary': f'חדר בריחה ל{name}',
      'description': f'טלפון: {phone}\nאימייל: {email}\nמספר אנשים: {amount}\nרמת קושי: {difficulty}',
      'start': {
        'dateTime': start_dt.isoformat(),
        'timeZone': 'Asia/Jerusalem',
      },
      'end': {
        'dateTime': end_dt.isoformat(),
        'timeZone': 'Asia/Jerusalem',
      },
    }

    event = service.events().insert(calendarId=calenderID, body=event).execute()
    return event

def make_public_google_calendar_link(date_str, time_str):
    """
    Creates a universal 'Add to Google Calendar' link.
    start_dt and end_dt must be datetime objects (UTC or with tzinfo).
    """
    event = get_Specific_Event(date_str, time_str)
    start_dt = dateutil.parser.isoparse(event.get('start').get('dateTime'))
    end_dt = start_dt + timedelta(hours=1, minutes=30)

    start_str = start_dt.strftime("%Y%m%dT%H%M%S")
    end_str = end_dt.strftime("%Y%m%dT%H%M%S")

    base = "https://calendar.google.com/calendar/render"

    params = {
        "action": "TEMPLATE",
        "text": "חדר בריחה ל" + event.get("summary").split("ל")[-1],
        "dates": f"{start_str}/{end_str}",
        "duration": "T1H30M",
        "details": event.get("description")
    }

    return base + "?" + urllib.parse.urlencode(params)

# print(create_event(date='2025-10-23', time='14:00:00', difficulty='easy', email='jfhsdhf', name='name', phone='795438957394',amount=3,))
# tor = get_Specific_Event('2025-10-23', '14:00')
# print(tor)
