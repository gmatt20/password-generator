import random
import requests

# 19 long password: ***-***-***-***-***

response = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/hello")

data = response.json()

word = data[0]["word"]

print(word)

print(random.random() * 10)

