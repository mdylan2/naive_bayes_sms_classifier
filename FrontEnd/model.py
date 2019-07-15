from nltk.corpus import stopwords
import re

def textParser(text):
    tokens = re.sub('[!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]', "", text).split(" ")
    tokens = list(filter(lambda x: len(x) > 0 , map(str.lower,tokens)))
    tokens = list(filter(lambda x: x not in stopwords.words("english"),tokens))
    return tokens