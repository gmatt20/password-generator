from random_word import RandomWords
import random
import requests

# 19 long password: ***-***-***-***-***

randWord = RandomWords()

url = "https://api.dictionaryapi.dev/api/v2/entries/en/" + randWord.get_random_word()

response = requests.get(url)

data = response.json()

word = data[0]["word"]

print(word)

# print(random.random() * 10)

