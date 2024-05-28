import pytest
from unittest.mock import patch
from atividade05_get_data_from_api import get_data_from_api

@patch('atividade05_get_data_from_api.requests.get')
def test_get_data_from_api_success(mock_get):
    mock_response = mock_get.return_value
    mock_response.json.return_value = {'key': 'value'}
    url = 'http://fakeapi.com/data'

    data = get_data_from_api(url)
    assert data == {'key': 'value'}
    mock_get.assert_called_once_with(url)