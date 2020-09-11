def FrequentWordsWithMismatches_ReverseComplement(Text,k,d):
    Patterns=[]
    n=len(Text)
    freqMap={}
    for i in range(n-k):
        Pattern=Text[i:i+k]
        neighborhood=Neighbors(Pattern,d)
        for j in neighborhood:
            reverse_j=Reverse_dna_seq(j)
            if j not in freqMap:
                freqMap[j]=1
            else:
                freqMap[j] += 1
            if reverse_j not in freqMap:
                freqMap[reverse_j] = 1
            else:
                freqMap[reverse_j] += 1
                
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

def Reverse_dna_seq(Seq):
    Seq=Seq[::-1]
    Seq_reverse=[]
    for i in range(len(Seq)):
        if Seq[i]=="A":
            Seq_reverse.append("T")
        elif Seq[i]=="T":
            Seq_reverse.append("A")
        elif Seq[i]=="C":
            Seq_reverse.append("G")
        elif Seq[i]=="G":
            Seq_reverse.append("C")
    Seq=''.join(Seq_reverse)
    return Seq
