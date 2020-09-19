from numpy import array as matrix, arange
import numpy as np

def greedy_motif_search_better(k,t,Dnas):
    '''use the greedy algorithm to find the motifs'''

    best_motif=[]
    motif=[]

    #construct best motifs from the first k-mer in each string
    for dna in Dnas:
        motifs=dna[0:k]
        best_motif.append(motifs)
        
    best_profile=profile(best_motif)
    best_consensus_string=consensus_string_finder(best_profile)
    
    for i in range(len(Dnas[0])-k+1):
        motif=[]
        motif.append(Dnas[0][i:i+k])
        for j in range(1,t):
            profile_matrix=profile(motif)
            motif.append(profile_most_probable_kmer(Dnas[j],k,profile_matrix))
        consensus_string=consensus_string_finder(profile(motif))

        motif_score=Score(motif,consensus_string)
        best_motif_score=Score(best_motif,best_consensus_string)

        if motif_score < best_motif_score:
            best_motif = motif
            best_consensus_string=consensus_string

    return best_motif

def profile(motifs):
    '''generate the profile matrix (4*k) of ACGT,
    and return the consensus string based on the most popular letter'''
    k=len(motifs[0])
    s=len(motifs)
    profile_matrix=np.ones((4,k)) #each element in the matrix is 1
    for motif in motifs:
        for j in range(0,k):
            if motif[j]=="A":
                profile_matrix[0,j]+=1
            if motif[j]=="C":
                profile_matrix[1,j]+=1
            if motif[j]=="G":
                profile_matrix[2,j]+=1
            if motif[j]=="T":
                profile_matrix[3,j]+=1
    profile_matrix=profile_matrix/(s+4)
    return profile_matrix


def consensus_string_finder(matrix):
    consensus_string=[]
    for i in range(matrix.shape[1]):
        popletter=[]
        for j in range(len(matrix[:,i])):
            if matrix[:,i][j]==np.max(matrix[:,i]):
                po = j
                if po==0:
                    popletter="A"
                elif po==1:
                    popletter="C"
                elif po==2:
                    popletter="G"
                elif po==3:
                    popletter="T"
                break
        consensus_string+=popletter[0]
    return ''.join(consensus_string)


def profile_most_probable_kmer(Text,k,profile):
    '''return the kmer with the biggest probable in text,
    profile is a matrix recording the possibility of ACGT'''
    max_probility_pattern=[]
    max_probility=0
    for i in range(len(Text)-k+1):
        pattern=Text[i:i+k]
        probility=1
        for j in range(len(pattern)):
            if pattern[j]=="A":
                p=profile[0,j]
                probility=probility*p
            elif pattern[j]=="T":
                p=profile[3,j]
                probility=probility*p
            elif pattern[j]=="G":
                p=profile[2,j]
                probility=probility*p
            elif pattern[j]=="C":
                p=profile[1,j]
                probility=probility*p
        if max_probility < probility:
            max_probility = probility
            max_probility_pattern=pattern
    if max_probility == 0:
        max_probility_pattern=Text[0:k]
    return max_probility_pattern        

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

def Score(motifs,consensus_string):
    """return the distances between motifs and the consensus_string"""
    distances=0
    for motif in motifs:
        d=HammingDistance(motif,consensus_string)
        distances+=d
    return distances

Dnas=["GGCGTTCAGGCA","AAGAATCAGTCA","CAAGGAGTTCGC","CACGTCAATCAC","CAATAATATTCG"]    
greedy_motif_search_better(3,5,Dnas)
