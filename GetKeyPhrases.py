import CognitiveTextFunctions as ctf

client = ctf.authenticate_client()

documents = ["My cat might need to see a veterinarian who lives in New York near the Chubb Insurance office."]

key_phrases = ctf.get_key_phrases(client, documents)
print("\tKey Phrases:")
for phrase in key_phrases:
    print("\t\t", phrase)
