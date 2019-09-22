print("Please wait while initiating...")
import re
import typing
from wordfreq import word_frequency
from nltk.stem import WordNetLemmatizer
from spacy.lemmatizer import Lemmatizer
from spacy.lang.en import LEMMA_INDEX, LEMMA_EXC, LEMMA_RULES
lemmatizer = Lemmatizer(LEMMA_INDEX, LEMMA_EXC, LEMMA_RULES)
import nltk
english_vocab = set(w.lower() for w in nltk.corpus.words.words())

from nltk.corpus import wordnet as wn
nouns = {x.name().split('.', 1)[0] for x in wn.all_synsets('n')}
adverbs = {x.name().split('.', 1)[0] for x in wn.all_synsets('r')}
verbs = {x.name().split('.', 1)[0] for x in wn.all_synsets('v')}
adjs = {x.name().split('.', 1)[0] for x in wn.all_synsets('a')}

wnl = WordNetLemmatizer()

stopwords = {
    'him', 'will', 'there', 'same', 'or', 'when', "you'll", 'should', 'this', 'has', 'yourselves', 'only', 'who', 'than', 'hasn', "mustn't", 'other', 'wouldn', 'most', "you're", 've', 'with', 'not', 'own', 'then', 'down', 'ain', 'which', 'up', 'was', 'off', 'have', "that'll", 'my', 'while', 'll', "it's", 'once', 'all', 'a', 'very', 'here', 'o', "didn't", 'themselves', 'isn', 'hadn', "should've", 't', 'having', 'that', 'from', "haven't", 'those', 'about', 'are', 'both', 'aren', 'we', 'her', "needn't", 'itself', 'where', 'as', "wouldn't", 'these', 'above', 'after', 'too', 'haven', 'its', 'to', 'ma', 'more', 'theirs', 'until', 'me', 'but', 'at', 'yours', "weren't", 'y', 'did', "isn't", "shan't", 'hers', 'such', 'through', 'of', 'himself', 's', 'can', 'an', 'whom', 'they', 'been', 'what', 'between', 'because', 'ourselves', 'into', 'wasn', 'herself', 'had', 'why', 'few', 'am', 'our', 'how', 'were', "don't", 'couldn', 'against', 'didn', 'don', "shouldn't", 'do', "doesn't", 'some', 'm', 'mightn', 'myself', 'doing', 'over', 'she', 
'during', 'just', 'won', 'further', 'each', 'be', 'now', 'by', "hadn't", 're', 'any', 'their', 'the', 'under', "won't", "you'd", "aren't", 'is', 'it', 'out', "you've", 'again', 'shan', 'i', "hasn't", 'mustn', 'does', 'being', 'his', 'if', 'yourself', 'on', 'you', "wasn't", 'shouldn', 'before', "mightn't", 'them', 'so', 'no', "couldn't", 'ours', 'nor', 'weren', 'in', "she's", 'doesn', 'for', 'your', 'he', 'd', 'and', 'below', 'needn'
}

from functools import lru_cache
memoize = lru_cache(None)
@memoize
def get_base_form(word: str):
    word = word.lower()
    verbcopy = lemmatizer(word,'VERB')[0]
    if verbcopy in verbs:
        return verbcopy
    if word in adjs:
        return word
    if word in adverbs:
        return word
    nouncopy = wnl.lemmatize(word)
    if nouncopy in nouns:
        return nouncopy
    return word

filename = input("Please move the file you would like to analyze into the reckoner folder and input the file name here. \n Don't forget the '.file_type' at the end! \n File Name: ")
eightPlus = open(filename,encoding="utf-8").read()
inputmin = input("You can delete every word that has appeared less than X times. Input 0 if you want to keep every word.\n Input X:")
inputmin = int(inputmin)
# print(processedText[10].text)

print("reading...")
'''splits the entire text into a list of words'''
textList = re.findall(r'\w+', eightPlus)
# print(textList)
# copyTextList = textList.copy()

occurence = dict()

# wordset = set()

print("creating instances...")
for word in textList:
    w = get_base_form(word.lower())
    occurence[w] = 0

for word in textList:
    occurence[get_base_form(word.lower())] += 1

copy_occ = dict()
for word, times in occurence.items():
    if len(word) == 1:
        continue
    if word in stopwords:
        continue
    if times < inputmin:
        continue
    copy_occ[word] = times

print("getting frequency...")
exclusive_words = dict()
delta = dict()
for word, times in copy_occ.items():
    freq = word_frequency(word, 'en',wordlist='large')*100000
    if not freq:
        exclusive_words[word] = times
    else:
        delta[word] = (times**1.7) / freq


print("sorting...")
every_word_sorted = sorted(copy_occ.items(), key = lambda x : x[1], reverse=True)
delta_sorted = sorted(delta.items(), key = lambda x : x[1], reverse=True)
exclusive_words_sorted = sorted(exclusive_words.items(), key = lambda x : x[1], reverse=True)
# print(every_word_sorted)

# print(sorted_dict)

s1='words_freq_'+filename
s2='ratio_to_overall_freq_'+filename
s3='new_words_freq_'+filename

f1 = open(s1,'w',encoding="utf-8")
print(*every_word_sorted,sep = "\n",file=f1)
f2 = open(s2,'w',encoding="utf-8")
print(*delta_sorted,sep = "\n",file=f2)
f3 = open(s3,'w',encoding="utf-8")
print(*exclusive_words_sorted,sep = "\n",file=f3)

print('done')


# textset = {'it'}
# for word in textList:
#     textset.add(lemmatizer.lemmatize(word.lower()))

# print(len(textset))

# f = open('out.txt','w',encoding="utf-8")
# print("lemmatized",file=f)
# for word in textset:
#     print(word,file=f)