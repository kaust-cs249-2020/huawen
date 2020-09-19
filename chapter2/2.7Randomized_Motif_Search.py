import random
from numpy import array as matrix, arange
import numpy as np


def Randomized_Motif_Search(Dnas,k,t):
    '''use the Monte Carlo algorithms to find out the motifs in the Dnas'''

    #randomly select kmer motifs from each string in Dnas
    kmer_set_all=[]
    for dna in Dnas:
        kmer_set=[]
        for i in range(len(dna)-k+1):
            kmer=dna[i:i+k]
            kmer_set.append(kmer)
        kmer_set_all.append(kmer_set)
    motifs=[]
    for i in range(len(kmer_set_all)):
        motifs.append(random.choice(kmer_set_all[i]))
    best_motifs=motifs

    while True:
        profile_motif=profile(motifs)
        motifs=Motifs(profile_motif,Dnas)
        
        consensus_string=consensus_string_finder(profile_motif)
        best_consensus_string=consensus_string_finder(profile(best_motifs))

        if Score(motifs,consensus_string) < Score(best_motifs,best_consensus_string):
            best_motifs=motifs
        else:
            return best_motifs,Score(best_motifs,best_consensus_string)


def profile(motifs):
    '''generate the profile matrix (4*k) of ACGT,
    and return the consensus string based on the most popular letter'''
    k=len(motifs[0])
    s=len(motifs)
    profile_matrix=np.ones((4,k))
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

def profile_most_probable_kmer(Text,k,profile):
    '''return the kmer with the biggest probable in text,
    profile is a matrix recording the possibility of ACGT'''
    max_probability_pattern=[]
    max_probability=0
    for i in range(len(Text)-k+1):
        pattern=Text[i:i+k]
        probability=1
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
    if max_probability == 0:
        max_probability_pattern=Text[0:k]
    return max_probability_pattern

def Motifs(profilematrix,Dnas):
    k=len(profilematrix[0])
    motifs=[]
    for dna in Dnas:
        motifs.append(profile_most_probable_kmer(dna,k,profilematrix))
    return motifs

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

        
def runtime_randomized_motif_search(time):
    bestscore=float('inf')
    bestmotifs=[]
    for i in range(time):
        motifs,score=Randomized_Motif_Search(Dnas,k,t)
        if score<bestscore:
            bestscore=score
            bestmotifs=motifs
    for j in range(len(bestmotifs)):
        print(bestmotifs[j])
    return bestscore

Dnas=["CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA","GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG","TAGTACCGAGACCGAAAGAAGTATACAGGCGT",
      "TAGATCAAGTTTCAGGTGCACGTCGGTGAACC","AATCCACCAGCTCCACGTGCAATGTTGGCCTA"]
k=8
t=5
runtime_randomized_motif_search(1000)

