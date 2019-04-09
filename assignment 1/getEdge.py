import json
import pickle
from tqdm import tqdm


urls = pickle.load(open("url.pkl","rb"))
titles = pickle.load(open("title.pkl",'rb'))


egde_json = json.load(open("meta2.json","r"))

egde =[]


def getEgde():
    for e in egde_json:
        try:
            v1 = urls.index(e["from_url"].decode('utf-8'))
            v2 = urls.index(e["current_url"].decode('utf-8'))
            yield {'e': str(v1) + ":" + str(v2)}

        except:
            print("not in")


for e in getEgde():
    egde.append(e)


with open('egde.txt', 'w') as outfile:
    json.dump(egde, outfile)

