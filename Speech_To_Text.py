import json
from watson_developer_cloud import SpeechToTextV1

IBM_USERNAME = 'ffe50ef8-c55f-4d9e-a8ea-0c9baef786bf'
IBM_PASSWORD = 'gLanSzYAdxKr'

stt = SpeechToTextV1(username=IBM_USERNAME, password=IBM_PASSWORD)
audio_file = open("P5_interview.flac", "rb")


with open('transcript_result.json', 'wb') as fp:
    result = stt.recognize(audio_file, content_type="audio/flac",
                           continuous=True, timestamps=False,
                           max_alternatives=1)
    json.dump(result.result, fp)