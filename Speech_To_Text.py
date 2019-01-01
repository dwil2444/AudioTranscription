import json
from watson_developer_cloud import SpeechToTextV1

IBM_USERNAME = ''
IBM_PASSWORD = ''

stt = SpeechToTextV1(username=IBM_USERNAME, password=IBM_PASSWORD)
audio_file = open("<<filename.extension>>", "rb")


with open('transcript_result.json', 'wb') as fp:
    result = stt.recognize(audio_file, content_type="audio/flac",
                           continuous=True, timestamps=False,
                           max_alternatives=1)
    json.dump(result.result, fp)