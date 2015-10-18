## A LIBRARY MEANT FOR MOI'S DAILY PROGRAMMING 


def readtabtable(filename):
	table=open( filename,"r")
	cleanedtable=[x.replace("\n","").split("\t") for x in table]
	return cleanedtable


def listostring(list1):
# you have sth like ['A'] you get 'A'
    return str(list1).replace('[','').replace(']','').replace("'",'')



def findmostcommon(word):
# you have a string like 'AAAACAAAA' you get the most common letter, A as a 'A' string
    word=listostring(word)
    acceptedbases=["A",
               "G",
               "C",
               "T"]
    
    ase=word.count('A')
    ges=word.count('G')
    ces=word.count('C')
    tes=word.count('T')
    countings=[ase,ges,ces,tes]
    dictio={}
    for k, v in zip(acceptedbases, countings):
        dictio[k] = v
 
    mostcommon=list(base for base in dictio if dictio[base]==max(countings))
    return listostring(mostcommon)


def findleastcommon(word):
# you have a string like 'AAAACAAAA' you get the most common letter, A as a 'A' string
	word=listostring(word)
	acceptedbases=["A","G","C","T"]
	ase=word.count('A')
	ges=word.count('G')
	ces=word.count('C')
	tes=word.count('T')
	countings=[ase,ges,ces,tes]
	dictio={}
	for k, v in zip(acceptedbases, countings):
		dictio[k] = v
	leastcommon=list(base for base in dictio if dictio[base]>min(countings) and dictio[base]!=max(countings))
	return listostring(leastcommon)


def combinations(iterable, r):
#combinations('ABCD',2)-->ABACADBCBDCD
#combinations(range(4),3)-->012013023123
	pool=tuple(iterable)
	n=len(pool)
	if r>n:
		return
	indices=range(r)
	yield tuple(pool[i] for i in indices)
	while True:
		for i in reversed(range(r)):
			if indices[i] != i+n-r:
				break
		else:
			return
		indices[i]+=1
		for j in range(i+1,r):
			indices[j]=indices[j-1]+1
		yield tuple (pool[i] for i in indices)

