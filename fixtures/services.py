import pytest

from framework.calendar_service import CalendarService


@pytest.fixture
def calendar_service():
    """Initialize Google Calendar service api"""
    return CalendarService()
