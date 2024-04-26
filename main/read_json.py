import json
# Extracts all json descriptions into an array

def extract_claims(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        claim_numbers = [claim['ClaimNumber'] for claim in data]
        claim_descriptions = [claim['Description'] for claim in data]
    return claim_numbers, claim_descriptions