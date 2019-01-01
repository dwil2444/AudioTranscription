import os

os.system('python Speech_To_Text.py')  # Generate the json file with the data returned from the Watson Speech to text API
os.system('python Parse_Transcript.py') # Parse the json data and record the text in a .txt file