import pandas

import json
import pickle
json_data = json.load(open("meta.json","r"))

data =[]
title = []

for d in json_data:
    data.append(d['url'])
    title.append(d['title'])

pickle.dump(data,open("url.pkl","w"))
pickle.dump(title,open('title.pkl','w'))