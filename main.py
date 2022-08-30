# Importing necessary libraries
import requests
from pdf_to_text import PDFtoText

# Initializing PDFtoTxt object
path = PDFtoText("P:/School/Coding Courses/Python Journey/Day 90 - PDF to Audiobook/Hello World.pdf") # Path of PDF File to be converted
text_converted = path.generate_text()

# Endpoint of Voicerss API
endpoint_url = 'http://api.voicerss.org/'

# Declaration of parameters
params = {
    'key': '<API-KEY>', # 5cb9f19930d44f9dbce8018069b969fd
    'hl': 'en-us',
    'v': 'Linda',
    'src': text_converted,
    'r': '0',
    'c': 'mp3',
    'f': '8khz_8bit_stereo',
    'ssml': 'false',
    'b64': 'false'
}

# Sends and gets data from Voicerss
response = requests.get(endpoint_url, params=params)

# Prints out URL that directs user to the audio file accessible through the browser
print(response.url)
