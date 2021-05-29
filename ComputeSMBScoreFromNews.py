import CognitiveTextFunctions as ctf
import os

client = ctf.authenticate_client()

documents = ["The owner of two Boston-based construction companies has been indicted on charges of workers' compensation fraud in connection \
             with failing to obtain workers' compensation insurance, Attorney General Maura Healey announced today. \
            Christopher Rapczynski, age 48, of Andover, is the president of Sleeping Dog Properties, Inc. (SDP), and \
            New England Construction Resources (NECR). Rapczynski was indicted yesterday by a Suffolk County Grand Jury \
            on charges of Workers' Compensation Fraud (6 counts), Failure to Provide Workers' Compensation Insurance (1 count) \
            and Larceny Over $250 (5 counts). The arraignment is scheduled for a later date at Suffolk Superior Court. This \
            investigation was referred to the Attorney General's Office by the state's Insurance Fraud Bureau (IFB)."]

key_phrases = ctf.get_key_phrases(client, documents)
print("\tKey Phrases:")
for phrase in key_phrases:
    print("\t\t", phrase)

result = ctf.get_named_entities(client, documents)
print("Named Entities:\n")
for entity in result.entities:
    if entity.category == 'Organization':
        print("\tText: \t", entity.text, "\n\tCategory: \t", entity.category, "\tSubCategory: \t", entity.subcategory,
            "\tConfidence Score: \t", round(entity.confidence_score, 2), "\n") #"\tLength: \t", entity.length, "\tOffset: \t", entity.offset, "\n")

sentiments = ctf.get_sentiments(client, documents)
print("Document Sentiment: {}".format(sentiments.sentiment))
print("Overall scores: positive={0:.2f}; neutral={1:.2f}; negative={2:.2f} \n".format(
    sentiments.confidence_scores.positive,
    sentiments.confidence_scores.neutral,
    sentiments.confidence_scores.negative,
))