import boto3

def detect_text_resource(image_path: str):
    session = boto3.Session(profile_name='default')
    client = session.client('rekognition')
    with open(image_path, 'rb') as image_file:
        response = client.detect_text(
            Image={'Bytes': image_file.read()},
        )
    return response
