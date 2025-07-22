import json
import requests
import pandas as pd

if __name__ == '__main__':
  request_url = "https://api.gtfs-data.jp/v2/feeds"
  
  res = requests.get(request_url)
  
  resp = res.json()
  dataset = resp['body']
  #print(dataset)
  
  # json data
  with open('gtfs_repogitory_jp_feedlist.json', 'w', encoding = 'utf-8') as f:
    json.dump(dataset, f, indent=2, ensure_ascii=False)
  
  # json to csv
  df = pd.json_normalize(dataset)
  df.to_csv('gtfs_repogitory_jp_feedlist.csv', encoding = 'utf-8')
  
  print("Finished.")
