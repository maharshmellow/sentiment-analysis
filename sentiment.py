# necessary libraries: nltk

from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *

n_instances = 100
subj_docs = [(sent, "subj") for sent in subjectivity.sents(categories="subj")[:n_instances]]
obj_docs = [(sent, "obj") for sent in subjectivity.sents(categories="obj")[:n_instances]]
print(len(subj_docs), len(obj_docs))

print(subj_docs[0]) # shows the first tokenized subjective movie review


train_subj_docs = subj_docs[:80]
test_subj_docs = subj_docs[80:100]
train_obj_docs = obj_docs[:80]
test_obj_docs = obj_docs[80:100]

training_docs = train_subj_docs + train_obj_docs
testing_docs = test_subj_docs + test_obj_docs

sentim_analyzer = SentimentAnalyzer()
all_words_neg = sentim_analyzer.all_words([mark_negation(doc) for doc in training_docs])        # mark_negation puts a _NEG suffix to words that appear between a negation and a punction mark
