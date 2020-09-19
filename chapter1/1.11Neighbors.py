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


def ImmediateNeighbors(Pattern):
    '''return the sequense which distances is 1 to the pattern,
    containing pattern'''
    Neighborhood=[]
    subs=["A","G","T","C"]
    for i in range(len(Pattern)):
        symbol=Pattern[i]
        for k in subs:
            if symbol != k:
               Neighbor = Pattern[:i]+k+Pattern[i+1:]
               Neighborhood.append(Neighbor)
            else:
                Neighborhood.append(Pattern)
    final_Neighborhood=[]
    for n in range(len(Neighborhood)):
        if Neighborhood[n] not in final_Neighborhood:
            final_Neighborhood.append(Neighborhood[n])
    return final_Neighborhood
