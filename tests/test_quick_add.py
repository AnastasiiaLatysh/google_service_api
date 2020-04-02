from random import choice

import pytest

from test_data.caelndar_event_data import acceptable_values_for_param, error_messages
from test_data.random_data import get_random_string_with_digits


@pytest.mark.parametrize('optional_params', [{}, {"sendUpdates": choice(acceptable_values_for_param['sendUpdates'])}],
                         ids=['only required params', 'with optional params'])
def test_added_event_only_required_params(calendar_service, optional_params):
    event_summary = get_random_string_with_digits()
    calendar_event = calendar_service.quick_add(event_summary, **optional_params)
    assert calendar_event['summary'] == event_summary, 'Event was created with wrong summary'


def test_fetch_created_event(calendar_service):
    calendar_event = calendar_service.quick_add(get_random_string_with_digits())
    fetched_event = calendar_service.fetch_event(calendar_event['id'])
    assert fetched_event['id'] == calendar_event['id'], 'Wrong calendar event was fetched by id'
    assert fetched_event == calendar_event, 'Fetched calendar event data differs from the created one'


def test_add_event_to_wrong_calendar(calendar_service):
    response = calendar_service.quick_add(get_random_string_with_digits(), calendar_id=1)
    assert "id" not in response, 'Calendar event was created for wrong calendar'
    assert response['status_code'] == 404, 'Wrong status code received'


def test_wrong_value_for_optinal_param(calendar_service):
    param_value = get_random_string_with_digits()
    response = calendar_service.quick_add(get_random_string_with_digits(), sendUpdates=param_value)
    assert response == error_messages['not_allowed_value_for_param'].format(
        'sendUpdates', param_value, acceptable_values_for_param['sendUpdates']), 'Incorrect error message received'
