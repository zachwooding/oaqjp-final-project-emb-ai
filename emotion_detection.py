# final_project/emotion_detection.py

import requests

def emotion_detector(text_to_analyze):
    # URL for the Emotion Predict service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Headers for the request
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    
    # Input JSON payload
    data = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    # Send a POST request to the service
    response = requests.post(url, headers=headers, json=data)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Return the text attribute of the response object
        return response.json().get('text')
    else:
        # Handle errors or unsuccessful responses
        response.raise_for_status()
