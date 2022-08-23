import syllapy
import json

with open('JSON FILE OUTPUT.json', 'r') as f:
    syllables = json.load(f)

with open('TXT FILE OF WORDS', 'r') as f:
    for line in f.readlines():
        syllablecount = syllapy.count(line.strip())
        if syllables[str(syllablecount)]:
            syllables[str(syllablecount)].append(line.strip())
        else:
            syllables[str(syllablecount)] = [line.strip()]

with open('JSON FILE OUTPUT', 'w') as f:
    json.dump(syllables, f)
