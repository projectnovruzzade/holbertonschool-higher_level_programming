#!/usr/bin/env python3
from task_02_csv import csv_to_json

csv_file = "data.csv"
csv_to_json(csv_file)
print(f"Data from {csv_file} has been converted to data.json")