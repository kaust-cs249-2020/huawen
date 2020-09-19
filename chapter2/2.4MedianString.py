
def k_pattern(k):
    #generate k-mer pattern from {A,G,T,C}
    nucletide=["A","G","C","T"]
    final_output=[]
    if k==1:
        return nucletide
    else:
        output=k_pattern(k-1)
        for i in range(len(nucletide)):
            for j in range(len(output)):
                final_output.append(nucletide[i]+output[j])
    return final_output

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


def distance_dnas_pattern(pattern,dnas):
    '''return the minimum distance between pattern and
    pattern' from all of the dna strings in list dnas
    '''
    k=len(pattern)
    final_d=0
    for dna in dnas:
        dd=k
        for i in range(len(dna)-k+1):
            dnaa=dna[i:i+k]
            d=HammingDistance(pattern,dnaa)
            if d<dd:
                dd=d
        final_d+=dd
    return final_d

def MedianString(Dna,k):
    '''return the kmer pattern which have a minimum distance
    with all of the dna'''
    distance=float("inf")
    patterns=k_pattern(k)
    median=[]
    for pattern in patterns:
        d = distance_dnas_pattern(pattern,Dna)
        if distance > d:
            distance = d
            median = pattern
    return median




