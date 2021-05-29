import CognitiveTextFunctions as ctf

client = ctf.authenticate_client()

documents = ["Ce document est rédigé en Français."]

language = ctf.get_language(client, documents)
print("Language: ", language.primary_language.name)

