import random
from numpy import array as matrix, arange
import numpy as np

def Gibbs_Sampler(Dnas,k,t,N):
    '''find out the kmer motifs in the Dnas'''

    #randomly select kmers motifs
    kmer_set_all=[]
    for dna in Dnas:
        kmer_set=[]
        for i in range(len(dna)-k+1):
            kmer=dna[i:i+k]
            kmer_set.append(kmer)
        kmer_set_all.append(kmer_set)
        
    randomly_select_kmer=[]
    for i in range(len(kmer_set_all)):
        randomly_select_kmer.append(random.choice(kmer_set_all[i]))

    best_motifs=randomly_select_kmer

    for j in range(1,N):
        i=random.randint(0,t-1)#randomly choose a number i
        motif_i=randomly_select_kmer.pop(i)#delete the i-th motif in motifs
        profile_del_motif_i=profile(randomly_select_kmer)#generate the profile based on the updated motifs
        motif_i=profile_randomly_generated_kmer(Dnas[i],k,profile_del_motif_i)#generate the i-th motif in Dnas[i] base on the profile
        randomly_select_kmer.insert(i,motif_i)


        best_profile_motifs=profile(best_motifs)
        best_consensus_string=consensus_string_finder(best_profile_motifs)
        profile_motifs=profile(randomly_select_kmer)
        consensus_string=consensus_string_finder(profile_motifs)

        best_score=Score(best_motifs,best_consensus_string)
        motif_score=Score(randomly_select_kmer,consensus_string)

        if best_score>motif_score:
            best_motifs=randomly_select_kmer
            best_score=motif_score
    return best_motifs,best_score

def profile_randomly_generated_kmer(Dna,k,profile):
    kmer_possibility=[]
    kmer_pattern=[]
    for n in range(len(Dna)-k+1):
        pattern=Dna[n:n+k]
        kmer_pattern.append(pattern)
        possibility=1
        for j in range(k):
            if pattern[j]=="A":
                p=profile[0,j]
                possibility=possibility*p
            elif pattern[j]=="C":
                p=profile[1,j]
                possibility=possibility*p
            elif pattern[j]=="G":
                p=profile[2,j]
                possibility=possibility*p
            elif pattern[j]=="T":
                p=profile[3,j]
                possibility=possibility*p
        kmer_possibility.append(possibility)

    sum_possibility=sum(kmer_possibility)
    kmer_possibility=np.array(kmer_possibility)/sum_possibility
    kmer_number=range(len(kmer_possibility))

    #according to the kmer_possibility,randomly generate a number refering to the position in kmer_pattern
    randomly_generated_kmer_number=np.random.choice(kmer_number,p=kmer_possibility.ravel())

    return kmer_pattern[randomly_generated_kmer_number]



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

def Score(motifs,consensus_string):
    """return the distances between motifs and the consensus_string"""
    distances=0
    for motif in motifs:
        d=HammingDistance(motif,consensus_string)
        distances+=d
    return distances

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

def runtime_gibbssampler(time):
    bestmotifs=[]
    bestscore=float("inf")
    for i in range(time):
        motifs,score=Gibbs_Sampler(Dnas,k,t,N)
        if score<bestscore:
            bestscore=score
            bestmotifs=motifs
    for j in range(len(bestmotifs)):
        print(bestmotifs[j])
    return bestscore
    
Dnas=["CGCCCCTCTCGGGGGTGTTCAGTAACCGGCCA","GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG","TAGTACCGAGACCGAAAGAAGTATACAGGCGT",
      "TAGATCAAGTTTCAGGTGCACGTCGGTGAACC","AATCCACCAGCTCCACGTGCAATGTTGGCCTA"]

k=8
t=5
N=100

runtime_gibbssampler(20)
