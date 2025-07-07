from google.oauth2 import service_account
from googleapiclient.discovery import build

SERVICE_ACCOUNT_FILE = 'credentials/service_account.json'
SCOPES = ['https://www.googleapis.com/auth/calendar']


credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

service = build('calendar', 'v3', credentials=credentials)


calendar = {
    'summary': 'Assistant Booking Calendar',
    'timeZone': 'Asia/Kolkata'
}

created_calendar = service.calendars().insert(body=calendar).execute()

print("✅ New calendar created!")
print("🆔 Calendar ID:", created_calendar['id'])
