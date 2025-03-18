import json
import datasets
import ast  # Import for safe conversion

def process_docs(dataset: datasets.Dataset) -> datasets.Dataset:
    """
    Processes the dataset by ensuring JSON fields use proper formatting.
    Converts the 'tokens' field from a JSON-like string to a valid JSON object.
    """
    def _process_doc(doc):
        if isinstance(doc["tokens"], str):
            try:
                # Use ast.literal_eval to safely convert single-quoted JSON to Python objects
                tokens_list = ast.literal_eval(doc["tokens"])
                
                # Ensure it's converted into a proper JSON-compatible format
                doc["tokens"] = json.loads(json.dumps(tokens_list))  # Convert to valid JSON
                
            except (SyntaxError, ValueError) as e:
                print(f"Error decoding JSON: {e} \nProblematic Entry: {doc['tokens']}")
                doc["tokens"] = []  # Fallback to empty list if parsing fails
        
        return doc

    return dataset.map(_process_doc)
