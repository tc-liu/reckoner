# reckoner
Analyzes file-specific stylistic diction

# Features:
- Sorts and outputs the frequency of each word, different forms of a word counts as one word.
- Compares, sorts and outputs the word frequency of the word in this file to the overall frequency of the file in the file's language
- Sorts and outputs the words that have only appeared in this text file. 
- Changes every word to its base form: riding --> ride, stories -> story
- Lightning fast algorithm: analysis of a 600,000 word file can be delivered within a second

# Installing dependencies:
Installing from pip:
```markdown
pip install wordfreq
pip install nltk
pip install spacy
```
Note that wordfreq may need you to install [C++ Build Tools](https://go.microsoft.com/fwlink/?LinkId=691126)
