from numpy import array as matrix, arange

def profile_most_probable_kmer(Text,k,profile):
    '''from a given profile, generate the kmer pattern with
    the biggest probability from Text
    '''
    max_probability_pattern=[]
    max_probability=0
    for i in range(len(Text)-k+1):
        pattern=Text[i:i+k]
        probabiility=1
        for j in range(len(pattern)):
            if pattern[j]=="A":
                p=profile[0,j]
                probability=probability*p
            elif pattern[j]=="T":
                p=profile[3,j]
                probability=probability*p
            elif pattern[j]=="G":
                p=profile[2,j]
                probability=probability*p
            elif pattern[j]=="C":
                p=profile[1,j]
                probability=probability*p
        if max_probability < probability:
            max_probability = probability
            max_probability_pattern=pattern
    return max_probability_pattern
            
