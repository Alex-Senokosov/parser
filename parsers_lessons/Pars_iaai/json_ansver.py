import requests
import json

url = 'https://store.playstation.com/en-us/product/UP0082-CUSA33821_00-FF2PS4APPNA00001'
response = requests.get(url)

if response.status_code == 200:
    content_type = response.headers['content-type']
    if 'application/json' in content_type:
        json_data = response.json()
        print(json_data)
    else:
        print('Error: Content-Type is not application/json')
else:
    print('Error:', response.status_code)
