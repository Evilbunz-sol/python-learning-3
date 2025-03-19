import requests
import json

facebook_token = "test"

url = f"https://graph.facebook.com/v13.0/105360698771730?fields=link%2Cimages&access_token={facebook_token}"

response = requests.get(url)
data = response.text

data = json.loads(data)
image_url = data['images'][0]['source']

image_bytes = requests.get(image_url).content

with open('image.jpg', 'wb') as file:
  file.write(image_bytes)