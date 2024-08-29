import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    #Input 
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)
     # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)    
    
    # Extracting emotions, including anger, disgust, fear, joy and sadness, along with their scores.
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']

    # Finding the dominant emotion
    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }

    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    dominant_score = emotion_scores[dominant_emotion]

    # Returning a dictionary containing sentiment analysis results
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }