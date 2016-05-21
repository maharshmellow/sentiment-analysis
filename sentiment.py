# necessary libraries: nltk

from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *

n_instances = 500
subj_docs = [(sent, "subj") for sent in subjectivity.sents(categories="subj")[:n_instances]]
obj_docs = [(sent, "obj") for sent in subjectivity.sents(categories="obj")[:n_instances]]
print(len(subj_docs), len(obj_docs))

print(subj_docs[0]) # shows the first tokenized subjective movie review


train_subj_docs = subj_docs[:100]
test_subj_docs = subj_docs[100:500]
train_obj_docs = obj_docs[:100]
test_obj_docs = obj_docs[100:500]

training_docs = train_subj_docs + train_obj_docs
testing_docs = test_subj_docs + test_obj_docs

sentim_analyzer = SentimentAnalyzer()
all_words_neg = sentim_analyzer.all_words([mark_negation(doc) for doc in training_docs])        # mark_negation puts a _NEG suffix to words that appear between a negation (not, didn't...) and a punction mark

unigram_feats = sentim_analyzer.unigram_word_feats(all_words_neg, min_freq=4)                   # returns the top words/tokens sorted by frequency

sentim_analyzer.add_feat_extractor(extract_unigram_feats, unigrams=unigram_feats)

training_set = sentim_analyzer.apply_features(training_docs)
test_set = sentim_analyzer.apply_features(testing_docs)

trainer = NaiveBayesClassifier.train
classifier = sentim_analyzer.train(trainer, training_set)

for key, value in sorted(sentim_analyzer.evaluate(test_set).items()):
    print('{0}: {1}'.format(key, value))
