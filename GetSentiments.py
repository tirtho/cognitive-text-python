import CognitiveTextFunctions as ctf

client = ctf.authenticate_client()

documents = ["I had the best day of my life. I wish you were there with me."]

sentiments = ctf.get_sentiments(client, documents)
print("Document Sentiment: {}".format(sentiments.sentiment))
print("Overall scores: positive={0:.2f}; neutral={1:.2f}; negative={2:.2f} \n".format(
    sentiments.confidence_scores.positive,
    sentiments.confidence_scores.neutral,
    sentiments.confidence_scores.negative,
))
for idx, sentence in enumerate(sentiments.sentences):
    print("Sentence: {}".format(sentence.text))
    print("Sentence {} sentiment: {}".format(idx+1, sentence.sentiment))
    print("Sentence score:\nPositive={0:.2f}\nNeutral={1:.2f}\nNegative={2:.2f}\n".format(
        sentence.confidence_scores.positive,
        sentence.confidence_scores.neutral,
        sentence.confidence_scores.negative,
    ))
