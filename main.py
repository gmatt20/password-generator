from random_word import RandomWords
import random

# 19 long password: ***-***-***-***-***

password = ""

for i in range(9):
  randWord = RandomWords()
  randNums = random.randint(100,999)
  if i % 3 == 0:
    password += randWord.get_random_word()
    password += "-"
  elif i % 2 == 0:
    password += str(randNums)
    password += "-"
print(password)

# print(random.random() * 10)

