import requests
import urllib, json
#response = urllib.urlopen("https://speech.googleapis.com/v1p1beta1/speech:recognize")
#data = json.loads(response.read())
#print(data)
url='https://speech.googleapis.com/v1p1beta1/speech:recognize'
import requests
r = requests.get(url)
print (r.json())
