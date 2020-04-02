from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from framework.base_google_service import BaseService
from utils.logger import logger


class CalendarService(BaseService):

    def __init__(self):
        super(CalendarService, self).__init__()
        self.service = build('calendar', 'v3', credentials=self.creds, cache_discovery=False)

    def quick_add(self, summary, calendar_id='primary', **kwargs):
        """
        Add event to calendar
        :param summary: (str) summary for calendar event
        :param calendar_id: (str) id of calendar to which event should be added
        :param kwargs: (dict) optional params with values (example, sendUpdates="none")
        :return: (dict) information of created event or parsed response in case calendar event was not created.
        """
        try:
            logger.debug(f"Add new event to calendar with calendar_id={calendar_id}, summary={summary} "
                         f"and optional params={kwargs}")
            return self.service.events().quickAdd(calendarId=calendar_id, text=summary, **kwargs).execute()
        except HttpError as http_error:
            logger.debug(f"HTTPError occurred during calendar event creation. Response is: {http_error}")
            return {"status_code": int(http_error.resp['status'])}
        except TypeError as error:
            logger.debug(f"TypeError occurred during calendar event creation. Response is: {error}")
            return error.args[0]

    def fetch_event(self, event_id, calendar_id='primary'):
        logger.debug(f"Fetch calendar event by calendar_id={calendar_id} and event_id={event_id}")
        return self.service.events().get(calendarId=calendar_id, eventId=event_id).execute()
