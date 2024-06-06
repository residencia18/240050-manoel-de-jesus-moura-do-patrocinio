import pytest
from unittest.mock import Mock
import sys
import os 

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from atividade14_email_service import EmailService,EventHandler

# ----- ROTINA DE TESTE -------

# Verificação se o método send_email é chamado corretamente.
# Mocking do serviço EmailService para verificar a interação com EventHandler.


def test_handle_event_calls_send_email(mocker):
    mock_email_service = mocker.Mock(spec=EmailService)
    event_handler = EventHandler(mock_email_service)
    event = {"key": "value"}
    
    event_handler.handle_event(event)
    
    mock_email_service.send_email.assert_called_once_with(
        'test@example.com', 'Event Occurred', str(event)
    )