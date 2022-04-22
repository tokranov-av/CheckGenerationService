import json
import requests
import os
from check_generation_service.settings import BASE_DIR, MEDIA_ROOT
import base64

url = 'http://localhost:49153/'
html_file_path = os.path.join(BASE_DIR, 'templates', 'client_check.html')

data = {
    'contents': open(html_file_path, encoding='utf-8').read().encode('base64'),
}
headers = {
    'Content-Type': 'application/json',    # This is important
}
response = requests.post(url, data=json.dumps(data), headers=headers)
print(response)
# Save the response contents to a file
# with open('file.pdf', 'wb') as f:
#     f.write(response.content)
