import json
# Extracts all json descriptions into an array

file_path = './claims_data.json'



with open(file_path, 'r') as file:
    data = json.load(file)
    claim_descriptions = [claim['Description'] for claim in data]


print(claim_descriptions)

