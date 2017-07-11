import nltk
import re
import math
import operator



ch=[['Chinese','Deijing','Chinese'],['Chinese','Chinese','Shanghai'],['Chinese','Macao']]
ja=[['Tokyo','Japan','Chinese']]
allclasses=[ch,ja]
test=[['Chinese','Chinese','Chinese','Tokyo','Japan']]
classafterfilter=[]
chwords=[]
jawords=[]
testword=[]
allclasseswords=[]

for llist in allclasses:
	for sublist in llist:
		for word in sublist:
			if sublist.count(word)>1:
				sublist.remove(word)
		print sublist
		

for ll in test:
        for lllist in ll:
                if ll.count(lllist)>1:
                        ll.remove(lllist)
        print ll

        
for i in ch:
    for word in i:
        chwords.append(word)
print chwords 
for k in ja:
    for word2 in k:
        jawords.append(word2)
print jawords 
        


for m in test:
        for word3 in m:
                testword.append(word3)
print testword 

for h in allclasses:
        for listl in h:
                for word4 in listl:
                        allclasseswords.append(word4)
print allclasseswords
                
    

def classification(testword):
        vlist=[]
        v=0
        cnt=0
        solvingch=[]
        solvingja=[]
        A=0.0
        NC=0
        N=0
        NCA=[]
        prior=[]
        finalresultch=1
        finalresultja=1
        finallist=[]
        finalclass=[]
        classification={}
        theclass=""
        
        for c in allclasses:
                NC=len(c)
                text=""
                for d in c:
                        N=N+1
                NCA.append(NC)
        for cc in NCA:
                A=(float(cc)/float(N))
                prior.append(A)
        print prior
        
        for i in allclasseswords:
                if not i in vlist:
                        vlist.append(i)
        v=len(vlist)
        print v
        #trainig for chinees class
        for i in testword:
                if i in chwords:
                        cnt=float(chwords.count(i)+1.0)/float(len(chwords)+float(v))
                else:
                        cnt=float(0+1.0)/float(len(chwords)+float(v))
                solvingch.append(cnt)
        print solvingch
        #trainig for japan class
        for i in testword:
                if i in jawords:
                        cnt=float(jawords.count(i)+1.0)/float(len(jawords)+float(v))
                else:
                        cnt=float(0+1.0)/float(len(jawords)+float(v))
                solvingja.append(cnt)
        print solvingja
        #test solving
        for k in solvingch:
                finalresultch *=k
        finallist.append(finalresultch)
        for h in solvingja:
                finalresultja *=h
        finallist.append(finalresultja)

        
        print finallist
        #final list and classification
        for i in range(0, len(prior)):
                finalclass.append(prior[i]*finallist[i])
        print finalclass
        #the real class
        classification.setdefault('class chiness',[]).append(finalclass[0])
        classification.setdefault('class japan',[]).append(finalclass[1])
        theclass=max(classification.iteritems(), key=operator.itemgetter(1))[0]
        print theclass
        

        
        
        
                        

       

        
                        
        
                
        
        
        
        

                                
                                
	
        
    
        
