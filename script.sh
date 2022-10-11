#!/bin/bash
echo "Running Prowler Scans"
./prowler -b -n -f <REGION_TO_MODIFY> -g cislevel1 -M csv -F
echo "Converting Prowler Report from CSV to JSON"
python converter.py
echo "Loading JSON data into DynamoDB"
python loader.py
