import os
import datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build
from dotenv import load_dotenv

load_dotenv()

SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = os.getenv("SERVICE_ACCOUNT_FILE")
CALENDAR_ID = os.getenv("GOOGLE_CALENDAR_ID")

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('calendar', 'v3', credentials=credentials)

def get_available_slots(date_str: str):
    try:
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        return ["Invalid date format, use YYYY-MM-DD"]

    slots = [
        datetime.datetime(date.year, date.month, date.day, 10),
        datetime.datetime(date.year, date.month, date.day, 11),
        datetime.datetime(date.year, date.month, date.day, 14),
        datetime.datetime(date.year, date.month, date.day, 15),
    ]

    return [slot.isoformat() for slot in slots]

def book_meeting(start_time: str, summary: str, email: str):
    try:
        datetime.fromisoformat(start_time)
    except ValueError:
        return "Invalid datetime format. Use ISO 8601 (e.g., 2025-07-09T17:00:00)."

    return (
        f"✅ Meeting successfully booked!\n"
        f"- Topic: {summary}\n"
        f"- Time: {start_time}\n"
        f"- Invite sent to: {email}"
    )

def book_slot(start_time, summary, email):
    start = datetime.datetime.fromisoformat(start_time)
    end = start + datetime.timedelta(minutes=30)

    event = {
        'summary': summary,
        'start': {'dateTime': start.isoformat(), 'timeZone': 'Asia/Kolkata'},
        'end': {'dateTime': end.isoformat(), 'timeZone': 'Asia/Kolkata'},
        'attendees': [{'email': email}],
    }

    service.events().insert(calendarId=CALENDAR_ID, body=event).execute()
    return "Booked successfully!"
