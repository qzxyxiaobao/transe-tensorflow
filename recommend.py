from preprocess import *
import numpy as np
import random

base_dir = "./weibo/"
e2id, rel2id = read_dic(base_dir)
id2e = {v:k for k,v in e2id.items()}
id2rel ={v:k for k,v in rel2id.items()}
sample = random.sample(e2id, 5)
e2vec = np.array(np.load('entity2vec.npy','r'))
r2vec = np.array(np.load('relation2vec.npy','r'))

for e in sample:
	distances = {}
	f=open(e,'w')
	f.write(e)
	f.write("\n\n")
	result = e2vec[e2id[e]]+r2vec[0]
	for id,e2 in enumerate(e2vec):
		distance = np.sum(np.abs(result-e2),dtype=np.float64)
		#print distance
		distances[id] = distance
	distances = sorted(distances.iteritems(), key = lambda a:a[1], reverse = False)
	for i in distances:
		print id2e[i[0]]
		f.write(id2e[i[0]])
		f.write('\t')
		print i[1].item()
		f.write(str(i[1].item()))
		f.write("\n")
	f.flush()
	f.close()


