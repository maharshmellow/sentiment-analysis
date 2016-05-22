import urllib.parse as up
import urllib.request

sentence = "dumb cow"

if sentence:
    argument = up.quote_plus(sentence)         # formats it as a proper url argument
    finalUrl = "http://ec2-54-191-21-155.us-west-2.compute.amazonaws.com/cgi-bin/sentiment.cgi?q=" + argument
    data = urllib.request.urlopen(finalUrl)
    value = float(str(data.read())[2:-3])

else:
    # empty sentence - no need to analyze it
    value = 0.0

print(value)
