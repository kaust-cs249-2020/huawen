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

def linearpeptide_Scoring(peptide,spectrum):
    '''score the spectrum and the ideal linear spectrum of peptide'''
    ideal_peptide_mass=linear_spectrum(peptide)
    score=0
    spectrum_new=spectrum[:]
    for i in ideal_peptide_mass:
        if i in spectrum_new:
            score+=1
            spectrum_new.remove(i)
    #print(score)
    return score

def trim(leaderboard,spectrum,N):
    ''' sorts all peptides in Leaderboard according to their scores,
    and then select the top N scoring peptides including ties
    return the N highest-scoring linear peptides on Leaderboard with respect to Spectrum'''
    if len(leaderboard)<=N:
        return leaderboard
    else:
        linear_scores=[]
        for i in range(len(leaderboard)):
            peptide=leaderboard[i]
            scores=linearpeptide_Scoring(peptide,spectrum)
            linear_scores.append((scores,i))
        #print(linear_scores)
        #linear_scores=sorted(linear_scores)
        linear_scores=sorted(linear_scores,key=lambda x:x[0],reverse=True)
        #print(linear_scores)
        #tradoff=linear_scores[-N]
        filter_leaderboard=[]
        for scores,i in linear_scores[:N]:
            filter_leaderboard.append(leaderboard[i])
        #for peptide in leaderboard:
        #    if linearpeptide_Scoring(peptide,spectrum)>=tradoff:
        #        filter_leaderboard.append(peptide)
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

spectrum=[57,57,71,99,129,137,170,186,194,208,228,265,285,299,307,323,356,364,394,422,493]
M=20

N=60

a=Convolution_Cyclopeptide_Sequencing(spectrum,N,M)

print('-'.join([str(i) for i in a]))

#peptide=[71,99,129,57,79,58]
#peptide=[99,71,137,57,72,57]
#print(linearpeptide_Scoring(peptide,spectrum))