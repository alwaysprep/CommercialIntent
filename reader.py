import csv

from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

import numpy

stop = [word.encode('utf-8') for word in stopwords.words('english')]

tokenizer = RegexpTokenizer(r'\w+')


def extract(file_name):
    data = {"text": [],
            "class": []}

    f = open(file_name, "r")

    reader = csv.reader(f, delimiter=',')

    for value, target in reader:
        tokens = []
        token = tokenizer.tokenize(value)
        for i in token:
            if i not in stop:
                tokens.append(i)

        value = " ".join(tokens).decode('cp1252', 'ignore')
        data["text"].append(value)
        data["class"].append(target)

    f.close()
    return data
