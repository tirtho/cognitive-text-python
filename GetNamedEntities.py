import CognitiveTextFunctions as ctf

client = ctf.authenticate_client()

documents = ["I had a wonderful trip to Redmond last week at the Microsoft campus"]
result = ctf.get_named_entities(client, documents)

print("Named Entities:\n")
for entity in result.entities:
    print("\tText: \t", entity.text, "\tCategory: \t", entity.category, "\tSubCategory: \t", entity.subcategory,
        "\n\tConfidence Score: \t", round(entity.confidence_score, 2), "\tLength: \t", entity.length, "\tOffset: \t", entity.offset, "\n")
