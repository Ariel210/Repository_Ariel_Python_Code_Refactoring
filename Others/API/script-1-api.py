import requests

url = 'https://www.google.com'
data_url = requests.get(url)

print(data_url)
