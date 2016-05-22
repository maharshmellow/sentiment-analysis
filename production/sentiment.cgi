#!/home/maharshmellow/anaconda3/bin/python3.5
# -*- coding: UTF-8 -*-

import cgitb
import os
import urllib.parse as up

from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize

cgitb.enable()




print("Content-Type: text/html;charset=utf-8")
print()
url = os.environ["REQUEST_URI"]
o = up.urlparse(url)

sentence = up.parse_qs(o.query)["q"][0]	# sentence = everything after "q="
# processing the sentence to get the sentiment values
sid = SentimentIntensityAnalyzer()
ss = sid.polarity_scores(sentence)
print(ss["compound"])
