def Spectral_Convolution(spectrum):
    '''generate the concolution of spectrum'''
    result=[]
    for i in range(len(spectrum)):
        for j in range(len(spectrum)):
            k=spectrum[j]-spectrum[i]
            if k>=57 and k<=200:
                result.append(k)
    return result

def count_spectral_convolution(spectrum,M):
    '''count the appearance times of the spectral convolution 
    select the top M spectral convolutions as the new alphabet
    '''
    convolution_list=Spectral_Convolution(spectrum)
    convolution_dict={}
    alphabet_new=[]
    if len(convolution_list)>=M:
        for i in set(convolution_list):
            convolution_dict[i]=convolution_list.count(i)
        tempt=sorted(convolution_dict.items(),key=lambda x:x[1],reverse=False)
        tradoff=tempt[-M][1]
        for i in tempt:
            if i[1]>=tradoff:
                alphabet_new.append(i[0])
        return alphabet_new
    else:
        return convolution_list

def Expand(peptide,alphabet_new):
    '''expand the peptide according to the new alphabet'''
    if peptide==[[]]:
        Final_peptides=[]
        for i in alphabet_new:
            Final_peptides.append([i])
        return Final_peptides  #a list
    else:    
        Final_peptides=[]
        for value in peptide:
            for mass in alphabet_new:
                sub_value=value.copy()
                sub_value.append(mass)
                Final_peptides.append(sub_value)
    return Final_peptides

def linear_spectrum(peptide):
    '''generate the linear spectrum of a peptide 
    peptide is a list of aa mass'''
    Linear_spectrum=peptide.copy()
    Linear_spectrum.append(0)
    for i in range(len(peptide)-1):
        for j in range(i+2,len(peptide)+1):
            Linear_spectrum.append(sum(peptide[i:j]))
        
    return sorted(Linear_spectrum)
'''
def linear_spectrum(peptide,alphabet_new):
    prefix_mass=[]
    prefix_mass.append(0)
    for i in range(0,len(peptide)):
        for j in alphabet_new:
            if j == peptide[i]:
                prefix_mass.append(prefix_mass[i]+alphabet_new[j])
    Linear_spectrum=[0]
    #print(len(prefix_mass))
    for i in range(len(peptide)):
        for j in range(i+1,len(peptide)+1):
            Linear_spectrum.append(prefix_mass[j]-prefix_mass[i])
            #print(i,j)
            #print(Linear_spectrum)
    return sorted(list(Linear_spectrum))
'''
def linearpeptide_Scoring(peptide,spectrum):
    '''score the spectrum and the ideal linear spectrum of peptide'''
    ideal_peptide_mass=linear_spectrum(peptide)
    score=0
    spectrum_new=spectrum[:]
    for i in ideal_peptide_mass:
        if i in spectrum_new:
            score+=1
            spectrum_new.remove(i)
    return score

def trim(leaderboard,spectrum,N):
    ''' sorts all peptides in Leaderboard according to their scores,
    and then select the top N scoring peptides including ties
    return the N highest-scoring linear peptides on Leaderboard with respect to Spectrum'''
    if len(leaderboard)<N:
        return leaderboard
    else:
        linear_scores=[]
        for i in range(len(leaderboard)):
            peptide=leaderboard[i]
            scores=linearpeptide_Scoring(peptide,spectrum)
            linear_scores.append(scores)
        linear_scores=sorted(linear_scores)
        tradoff=linear_scores[-N]
        filter_leaderboard=[]
        for peptide in leaderboard:
            if linearpeptide_Scoring(peptide,spectrum)>=tradoff:
                filter_leaderboard.append(peptide)
        return filter_leaderboard

def Convolution_Cyclopeptide_Sequencing(spectrum,N,M):
    leaderboard=[[]]
    leader_peptides=[]
    alphabet_new=count_spectral_convolution(spectrum,M)
    
    while len(leaderboard)!=0:
        leaderboard=Expand(leaderboard,alphabet_new)
        #print(leaderboard)
        for peptide_mass in leaderboard.copy():
            peptide_mass_sum=sum(peptide_mass)
            if peptide_mass_sum == spectrum[-1]:
                if linearpeptide_Scoring(peptide_mass,spectrum)>linearpeptide_Scoring(leader_peptides,spectrum):
                    leader_peptides=peptide_mass
            elif peptide_mass_sum > spectrum[-1]:
                leaderboard.remove(peptide_mass)
        leaderboard =trim(leaderboard,spectrum,N)
    return leader_peptides
'''
spectrum=[853,113,585,796,924,502,423,1210,342,186,761,391,593,1412,1152,1396,260,129,1381,229,242,
356,990,1047,57,748,1176,730,990,1038,1119,294,339,114,696,1251,1267,617,567,357,471,163,1266,1281,
0,536,1395,454,1104,1362,1039,892,1509,1086,129,649,1095,713,258,777,1394,753,299,599,648,876,414,
1249,813,242,859,1305,552,1284,861,650,1249,261,520,470,519,957,1233,405,260,861,762,810,1248,891,
916,1346,390,981,147,1323,390,732,618,1380,1038,756,989,225,633,910,204,1452,243,1119,860,1395,129,
57,503,1267,1153,276,462,228,1215,114,1170,357,973,388,519,699,131,128,1120,648,1452,1055,632,333,
1380,528,747,389,656,97,1167,779,1380,1280,942,115,1121,1152,1007,990,1006,1118,519,877,1378,471]
spectrum=sorted(spectrum)
'''
'''
spectrum=[]
with open("dataset_369297_7.txt",'r') as ff:
    for line in ff.readlines():
        spectrum.extend([int(i) for i in line.split()])
'''
spectrum=[57,57,71,99,129,137,170,186,194,208,228,265,285,299,307,323,356,364,394,422,493]
M=20#18

N=60#327

a=Convolution_Cyclopeptide_Sequencing(spectrum,N,M)

#print(Spectral_Convolution(spectrum))
print('-'.join([str(i) for i in a]))
#print(linear_spectrum([114,128,129,113]))