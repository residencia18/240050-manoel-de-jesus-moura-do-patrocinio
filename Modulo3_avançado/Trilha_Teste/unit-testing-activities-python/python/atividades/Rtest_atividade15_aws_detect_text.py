import pytest
import boto3
from moto import mock_rekognition
import json
import sys
import os 

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from atividade15_aws_detect_text import detect_text_resource

# ----- ROTINA DE TESTE -------

# Chamar a função com um caminho de imagem válido e verificar se o método detect_text do cliente AWS Rekognition é chamado corretamente.
# Mocking do cliente AWS Rekognition para verificar a interação sem realmente chamar o serviço AWS.


@pytest.fixture
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    boto3.setup_default_session(
        aws_access_key_id="test",
        aws_secret_access_key="test",
        aws_session_token="test",
        region_name="us-east-1"
    )

@pytest.fixture
def rekognition_client(aws_credentials):
    with mock_rekognition():
        client = boto3.client('rekognition')
        yield client

def test_detect_text_resource(monkeypatch, rekognition_client):
    # Load the example response from 'detect_text_response.json'
    with open('detect_text_response.json', 'r') as f:
        mock_response = json.load(f)
    
    # Define a mock function to replace the actual AWS call
    def mock_detect_text(Image):
        return mock_response
    
    # Use monkeypatch to replace the detect_text function with our mock
    monkeypatch.setattr(rekognition_client, 'detect_text', mock_detect_text)
    
    # Create a temporary image file for testing
    image_path = 'img-to-aws.jpg'
    
    # Call the function
    response = detect_text_resource(image_path)
    
    # Assert that the response matches the mock response
    assert response == mock_response