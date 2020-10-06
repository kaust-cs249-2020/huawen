#get the aa and mass dictionary
aa_integer_mass={}
with open('integer_mass_table.txt', 'r') as f1:
    for ip in f1.readlines():
        if ip != None:
            ip=ip.replace(" ",",")
            ip=ip.replace("\n","")
            ip=ip.split(",")
            for i in range(len(ip)):
                aa_integer_mass[ip[0]]=[int(ip[1])]

alphabet=list(aa_integer_mass.keys())

def linear_spectrum(peptide,alphabet,aa_integer_mass):
    '''return the linear spectrum of a given peptide'''
    #generate the linear peptide mass in peptide, eg NKEL,get N,NK,NKE,NKEL
    prefix_mass=[]
    prefix_mass.append(0)
    for i in range(0,len(peptide)):
        for j in alphabet:
            if j == peptide[i]:
                prefix_mass.append(prefix_mass[i]+int(aa_integer_mass[j][0]))
    Linear_spectrum=[0]
    #print(len(prefix_mass))
    for i in range(len(peptide)):
        for j in range(i+1,len(peptide)+1):
            Linear_spectrum.append(prefix_mass[j]-prefix_mass[i])
            #print(i,j)
            #print(Linear_spectrum)
    return sorted(list(Linear_spectrum))

def Expand(peptide):
    '''peptide is an empty list or dictionary with letters and mass
    this function is to expand peptide with 18 different aa'''
    if peptide==[""]:
        return aa_integer_mass
    else:    
        Final_peptides={}
        for key,value in peptide.items():#extract the character in peptide
            for aa,mass in aa_integer_mass.items(): #extract the 18 aa in alphabat,then stick each j to i
                new_key=key+aa
                sub_value=list(value)+mass
                Final_peptides[new_key]=sub_value
    return Final_peptides

def Linearpeptide_Scoring(Peptide, Spectrum):
    if Peptide==[""]:
        return 0
    else:
        peptide_mass=linear_spectrum(Peptide,alphabet,aa_integer_mass)
        score=0
        spectrum=Spectrum[:]
        for i in peptide_mass:
            if i in spectrum:
                score+=1
                spectrum.remove(i)
        return score

def trim(leaderboard,Spectrum,N):
    ''' sorts all peptides in Leaderboard according to their scores,
    and then select the top N scoring peptides including ties
    return the N highest-scoring linear peptides on Leaderboard with respect to Spectrum'''
    all_score_list={}
    output_peptides={}
    for key,value in leaderboard.items():
        all_score_list[key]=Linearpeptide_Scoring(key,Spectrum)
    score_list=sorted(list(all_score_list.values()))
    if len(score_list)>N:
        tradeoff=score_list[-N]
        for peptide,score in all_score_list.items():
            if score>=tradeoff:
                output_peptides[peptide]=leaderboard[peptide]
    else:
        for peptide,score in all_score_list.items():
            output_peptides[peptide]=leaderboard[peptide]
    return output_peptides

def Leaderboard_cyclopeptide_sequence(Spectrum,N):
    leaderboard=[""]
    leader_peptides=[""]
    #test=[]
    while len(leaderboard)!=0:
        leaderboard=Expand(leaderboard)
        #print(leaderboard)
        for peptide_key in list(leaderboard.keys()):
            peptide_mass=leaderboard[peptide_key]
            peptide_mass_sum=sum(peptide_mass)
            if peptide_mass_sum == Spectrum[-1]:
                if Linearpeptide_Scoring(peptide_key,Spectrum)>Linearpeptide_Scoring(leader_peptides,Spectrum):
                    leader_peptides=peptide_key
                    #test.append(leader_peptides)
            elif peptide_mass_sum > Spectrum[-1]:
                del leaderboard[peptide_key]
        leaderboard=trim(leaderboard,Spectrum,N)
    return leader_peptides


Spectrum=[0,71,113,129,147,200,218,260,313,331,347,389,460]
'''
with open("dataset_369295_8.txt",'r') as ff:
    for line in ff.readlines():
        Spectrum.extend([int(i) for i in line.split()])
'''
N=10
a=Leaderboard_cyclopeptide_sequence(Spectrum,N)
print(a) #a is a potential peptide string

for i in a:
    result=[]
    for j in i:
        result.append(aa_integer_mass[j][0])
    print('-'.join([str(z) for z in result]))
