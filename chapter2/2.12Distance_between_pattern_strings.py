def Distance_between_pattern_strings(Pattern,Dnas):
    k=len(Pattern)
    distance=0
    for dna in Dnas:
        hammingdistance=float('inf')
        for i in range(len(dna)-k+1):
            pattern=dna[i:i+k]
            if hammingdistance>HammingDistance(Pattern,pattern):
                hammingdistance=HammingDistance(Pattern,pattern)
        distance+=hammingdistance
    return distance

def HammingDistance(p,q):
    '''return the number of different characters between p and q'''
    if len(p) != len(q):
        print("Two strings' length are not equal!")
    else:
        distances=0
        for i in range(len(q)):
            if p[i] == q[i]:
                distances = distances
            else:
                distances += 1
    return distances
            
