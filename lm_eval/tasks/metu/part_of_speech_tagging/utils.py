import json
import datasets

def process_docs(dataset: datasets.Dataset) -> datasets.Dataset:
    """
    Processes the dataset by converting the 'tokens' field from a JSON-like string
    to a list of dictionaries. This ensures correct parsing for LM Evaluation Harness.
    """
    def _process_doc(doc):
        return {
            "sentence": doc["sentence"],
            "tokens": json.loads(doc["tokens"]) if isinstance(doc["tokens"], str) else doc["tokens"]
        }

    return dataset.map(_process_doc)
