import json


json_file='transcript_result.json'

json_data=open(json_file)
data = json.load(json_data)
with open('transcript.txt', 'a') as the_file:
    for x in range(len(data['results'])):
        if (x %2 == 0):
            the_file.write('Interviewer: ')
        else:
            the_file.write('Participant: ')
        the_file.write(data['results'][x]['alternatives'][0]['transcript'])
        the_file.write('\n')