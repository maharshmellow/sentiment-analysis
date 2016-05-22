from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize

sid = SentimentIntensityAnalyzer()


sentence = "Anushka is so stupid. She is a failure at life. "
print(sentence)
ss = sid.polarity_scores(sentence)

for i in sorted(ss):
    print(i, ":", ss[i])


sentence = "Cows are so cool. Cows are better than Anushka "
print(sentence)
ss = sid.polarity_scores(sentence)

for i in sorted(ss):
    print(i, ":", ss[i])


"""
Anushka is so stupid. She is a failure at life.
compound : -0.8256
neg : 0.523
neu : 0.477
pos : 0.0


Cows are so cool. Cows are better than Anushka
compound : 0.7088
neg : 0.0
neu : 0.543
pos : 0.457
"""
