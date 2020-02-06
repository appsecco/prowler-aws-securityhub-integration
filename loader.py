import boto3
import json
import decimal
import os

awsRegion = os.environ['AWS_REGION']
prowlerDynamoDBTable = os.environ['MY_DYANMODB_TABLE']

dynamodb = boto3.resource('dynamodb', region_name=awsRegion)

table = dynamodb.Table(prowlerDynamoDBTable)

# CHANGE FILE AS NEEDED
with open('format_prowler_report.json') as json_file:
    findings = json.load(json_file, parse_float = decimal.Decimal)
    for finding in findings:
        TITLE_ID = finding['TITLE_ID']
        TITLE_TEXT = finding['TITLE_TEXT']
        RESULT = finding['RESULT']
        NOTES = finding['NOTES']

        print("Adding finding:", TITLE_ID, TITLE_TEXT)

        table.put_item(
           Item={
               'TITLE_ID': TITLE_ID,
               'TITLE_TEXT': TITLE_TEXT,
               'RESULT': RESULT,
               'NOTES': NOTES,
            }
        )
