#!/usr/bin/python3
"""
Convert CSV data to JSON format
"""

import csv
import json


def convert_csv_to_json(filename):
    """
    Convert a CSV file to JSON format and save it to data.json
    """
    try:
        data = []

        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)

        with open('data.json', 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile)

        return True
    except Exception:
        return False
