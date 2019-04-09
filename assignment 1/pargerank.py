import pickle

import snap
import  json



edge = json.load(open("egde.txt","r"))

G1 = snap.TUNGraph.New()
urls = pickle.load(open("url.pkl","rb"))
titles = pickle.load(open("title.pkl",'rb'))
vertexts = []
for e in edge:
    v = e['e'].decode("utf-8").split(":")
    if v[0] not in vertexts:
        vertexts.append(v[0])
    if v[1] not in vertexts:
        vertexts.append(v[1])

for v in vertexts:
    G1.AddNode(int(v))


for e in edge:
    v = e['e'].decode("utf-8").split(":")
    G1.AddEdge(int(v[0]),int(v[1]))








PRankH = snap.TIntFltH()
snap.GetPageRank(G1, PRankH)

print len(PRankH)
print len(vertexts)
# PRankH = sorted(PRankH)
print type(PRankH)
f = open("raking.txt","w+")
f.write(titles[0].encode('utf-8')+"\t"+str(10158)+"\n")
f.write("PageRank"+"\t"+"Title")
for item in PRankH:
    print item, round(PRankH[item],4)
    f.write(titles[item].encode("utf-8")+"\t"+str(round(PRankH[item],4))+"\n")




