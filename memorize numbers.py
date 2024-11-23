import json

# Load the JSON file
with open('number_mnemonics.json', 'r') as file:
    mnemonics = json.load(file)

# Print the content
print(json.dumps(mnemonics, indent=4))
