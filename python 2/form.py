import pandas as pd
import requests
import json

with open('data.json', 'r') as json_file:
    data = json.load(json_file)

start_date = '2023-09-26'
end_date = '2023-09-30'
    
# Filter the records within the specified timeframe
filtered_data = [record for record in data if start_date <= record['date'] <= end_date]

for record in filtered_data:
    print(record)