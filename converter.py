import csv
import json

# Set variables for within container
CSV_PATH = 'output/prowler_report.csv'
JSON_PATH = 'output/prowler_report.json'

# Reads prowler CSV output
csv_file = csv.DictReader(open(CSV_PATH, 'r'))

# Create empty JSON list, read out rows from CSV into it
json_list = []
for row in csv_file:
    json_list.append(row)

# Writes row into JSON file, writes out to docker from .dumps
open(JSON_PATH, 'w').write(json.dumps(json_list))

# open newly converted prowler output
with open('output/prowler_report.json') as f:
    data = json.load(f)

# remove data not needed for Security Hub BatchImportFindings    
for element in data: 
    del element['PROFILE']
    del element['ITEM_SCORED']
    del element['ITEM_LEVEL']
    del element['ACCOUNT_NUM']
    del element['REGION']

# writes out to a new file, prettified
with open('output/format_prowler_report.json', 'w') as f:
    json.dump(data, f, indent=2)
