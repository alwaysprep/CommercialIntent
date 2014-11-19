import csv

from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

import numpy

stop = [word.encode('utf-8') for word in stopwords.words('english')]

tokenizer = RegexpTokenizer(r'\w+')

