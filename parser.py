from transformers import pipeline

ner = pipeline("ner", model="dslim/bert-base-NER", grouped_entities=True)

def parse_resume(text):
    entities = ner(text)

    name = []
    orgs = []
    
    for e in entities:
        if e["entity_group"] == "PER":
            name.append(e["word"])
        if e["entity_group"] == "ORG":
            orgs.append(e["word"])

    return {
        "Name": " ".join(name),
        "Organizations": list(set(orgs))
    }
