# generate set of syllabled words
# random words with those syllables
# bam, haiku
import json
import random
from tkinter.font import names

firstname = ""
lastname = ""

with open("english words syllables oscar.json", "r", encoding="utf-8") as file:
    syllables = json.load(file)
    file.close()

# selecting words with random number of syllables
# haiku has a 5-7-5 pattern

# number of syllables for each word
first_line = []
while sum(first_line) < 5:
    first_line.append(random.choice([i for i in range(1, 6 - sum(first_line)) if i != 7]))

second_line = []
while sum(second_line) < 7:
    second_line.append(random.choice([i for i in range(1, 8 - sum(second_line)) if i != 7]))

third_line = []
while sum(third_line) < 5:
    third_line.append(random.choice([i for i in range(1, 6 - sum(third_line)) if i != 7]))

# word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

first_line_words = []
second_line_words = []
third_line_words = []

for item in first_line:
    first_line_words.append(random.choice(syllables[str(item)]))

for item2 in second_line:
    second_line_words.append(random.choice(syllables[str(item2)]))

for item3 in third_line:
    third_line_words.append(random.choice(syllables[str(item3)]))

# generate first name and then last name
with open("firstnames.json", "r", encoding="utf-8") as file:
    fnames = json.load(file)
    file.close()
with open("lastnames.json", "r", encoding="utf-8") as file:
    lnames = json.load(file)
    file.close()

firstname = random.choice(fnames["firstnames"])
lastname = random.choice(lnames["lastnames"])  

first_line_words[0] = first_line_words[0].capitalize()
second_line_words[0] = second_line_words[0].capitalize()
third_line_words[0] = third_line_words[0].capitalize()

first_line_words = " ".join(first_line_words)
second_line_words = " ".join(second_line_words)
third_line_words = " ".join(third_line_words)

print("\n-------------------------------------\n")
print(first_line_words)
print(second_line_words)
print(third_line_words)
print(f"\n - {firstname} {lastname}, {random.randint(1800, 2020)}\n-------------------------------------\n")
