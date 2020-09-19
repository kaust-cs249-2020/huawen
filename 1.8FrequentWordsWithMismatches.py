def FrequentWordsWithMismatches(Text,k,d):
    Patterns=[]
    n=len(Text)
    freqMap={}
    for i in range(n-k+1):
        Pattern=Text[i:i+k]
        neighborhood=Neighbors(Pattern,d)
        for j in neighborhood:
            if j not in freqMap:
                freqMap[j]=1
            else:
                freqMap[j] += 1
    m=max(freqMap.values())
    for key,value in freqMap.items():
        if freqMap[key] == m:
            Patterns.append(key)
    return Patterns

def HammingDistance(p,q):
    distances=0
    if len(p) == len(q):
        for i in range(len(q)):
            if p[i] != q[i]:
                distances += 1
    return distances

def Neighbors(Pattern,d):
    subs=["A","G","T","C"]
    if d == 0:
        return [Pattern]
    if len(Pattern) == 1:
        return subs
    Neighborhood=[]
    SuffixNeighbors=Neighbors(Pattern[1:],d)
    for text in SuffixNeighbors:
        if HammingDistance(text,Pattern[1:]) < d:
            for k in subs: 
                Neighborhood.append(k+text)
        else:
            Neighborhood.append(Pattern[0]+text) 
    return Neighborhood
