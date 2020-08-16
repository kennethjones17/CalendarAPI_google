import pickle
import google_auth_oauthlib.flow
import googleapiclient.discovery
from apiclient.discovery import  build
from datetime import datetime,timedelta
starttime = datetime(2020,8,16,00,00)
endtime  = datetime(2020,8,16,23,59) # endtime = starttime + timedelta(hours=23)

scopes = ['https://www.googleapis.com/auth/calendar']#linking the API
client_secrets_file = 'client_secret_.json'

flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)#rendering the api to the securefile code
credentials = flow.run_console()
#print(credentials)
pickle.dump(credentials,open("token.pkl","wb"))
credentials = pickle.load(open("token.pkl","rb"))#saving the credential so we dont need to always connect it
service = build("calendar","v3",credentials=credentials)


result = service.calendarList().list().execute()
calendar_id = result['items'][0]['id']#listing the first Event in calendar
result = service.events().list(calendarId=calendar_id).execute()
result['items'][77]
#Creating a new Event using a template
timezone = 'Asia/Kolkata'
event = {
  'summary': 'BIrthday',
  'location': 'Bangalore',
  'description': 'WOOHOO',
  'start': {
    'dateTime': starttime.strftime("%Y-%m-%dT%H:%M:%S"),
    'timeZone': timezone,
  },
  'end': {
    'dateTime': endtime.strftime("%Y-%m-%dT%H:%M:%S"),
    'timeZone': timezone,
  },
  'reminders': {
    'useDefault': False,
    'overrides': [
      {'method': 'email', 'minutes': 24 * 60},
      {'method': 'popup', 'minutes': 10},
    ],
  },
}
  
#service.events().insert(calendarId = calendar_id,body=event).execute()
event = service.events().insert(calendarId='primary', body=event).execute()#executing template to create new event
print ('Event created: %s' % (event.get('htmlLink'))


# =============================================================================
# if not events:
#         print('No upcoming events found.')
# for event in events:
#     start = event['start'].get('dateTime', event['start'].get('date'))
#     print(start, event['summary'])
# =============================================================================
# =============================================================================
# 
# from apiclient.discovery import  build
# from google_auth_oauthlib.flow import InstalledAppFlow
# 
# scopes = ['https://www.googleapis.com/auth/calendar']
# 
# flow = InstalledAppFlow.from_client_secrets_file("client_secret_.json",scopes='scopes')
# flow.run_console()
#  
# 
# =============================================================================


