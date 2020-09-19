def MotifEnumeration(Dna,k,d):
    '''use a brute force approach to find the implanted motifs
    Dna: several dna strings
    k: length of the pattern
    d: number of dismatches
    '''
    Pattern=[]
    for i in range(len(Dna)):
        dna=Dna[i]
        for j in range(len(dna)-k):
            pattern=dna[j:j+k]
            neighbor_pattern=Neighbors(pattern,d)
            for neighbor in neighbor_pattern:
                count=0
                for m in Dna:
                    if Count_d(neighbor,m,d)>0: #count number of neighbors that have at most d dismatches with dna
                        count+=1
                if count==len(Dna):#judge whether the neighbor appear in each string or not
                    Pattern.append(neighbor)
    final_pattern=[]
    for o in Pattern:#remove the duplicate from Pattern
        if o not in final_pattern:
            final_pattern.append(o)
    return final_pattern

def Neighbors(Pattern,d):
    '''generate the neighbors of pattern with at most d mismatch
    operation time: O(n^d)
    n: length of the pattern
    '''
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

def HammingDistance(p,q):
    '''return the distance between p and q
    operation time: O(len(p))
    '''
    distances=0
    if len(p) == len(q):
        for i in range(len(q)):
            if p[i] != q[i]:
                distances += 1
    return distances

def Count_d(Pattern,Text,d):
    '''return the appear times of a pattern with at most d mismatich in a Text
    operation time: O((len(Text)-len(pattern))*len(pattern))
    ''' 
    L=len(Pattern)
    count=0
    for i in range(len(Text) - L + 1):
        compare_string=Text[i:i+L]
        distance=0
        for j in range(len(Pattern)):
            if Pattern[j] != compare_string[j]:
                distance+=1
        if distance <= d:
            count += 1
    return count
