# haiku-writer
An automatic haiku generator so I can prove how dumb poetry is

I started with a list of 3,000 english words from https://www.ef-australia.com.au/english-resources/english-vocabulary/top-3000-words/, and then converted them into a json file with their respective number of syllables using Syllapy.

After that I found a couple csv's of first and last names to generate names with from here: https://raw.githubusercontent.com/hadley/data-baby-names/master/baby-names.csv and here: https://github.com/fivethirtyeight/data/raw/master/most-common-name/surnames.csv

Essentially I just converted these into JSON files for easy access, and then the code generates a random sequence of syllables for each line, finds random words with those syllables and then generates a haiku based on that.

### Running

`python3 -m "haiku-writer" v2.py`

If you want to use txtconverter you will also need to `pip install syllapy`

If you want to use a different list of words, use txtconverter.py to convert them. Use a txt file of words seperated each on a new line, and then create an empty json for the results.
