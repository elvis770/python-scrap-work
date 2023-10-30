import pandas as pd
import requests
import json

api_url = 'https://v1.nocodeapi.com/elvis770/fit/zgKqRhhRJsXHbhJI/aggregatesDatasets?dataTypeName=calories_expended'

response = requests.get(api_url)

if response.status_code == 200:
         
         data = response.json()
         
         with open("data.json", "w") as outflie:
             json_object = json.dumps(data)
             outflie.write(json_object)
         print(data)
        
else:
    
    print(f"APi request failed with status code{response.status_code}")