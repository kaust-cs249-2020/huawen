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
#print(aa_integer_mass)

alphabet=list(aa_integer_mass.keys())
#aa_integer_mass[""]=0

def Expand(peptide):
    '''peptide is an empty list or dictionary with letters and mass'''
    if peptide==[""]:
        return aa_integer_mass
    else:    
        Final_peptides={}
        for key,value in peptide.items():#extract the character in peptide
            for aa,mass in aa_integer_mass.items(): #extract the 18 aa in alphabat,then stick each aa to character in peptide
                new_key=key+aa
                sub_value=list(value)+mass
                Final_peptides[new_key]=sub_value
    return Final_peptides

#print(Expand([""]))

def cyclic_spectrum(peptide,alphabet,aa_integer_mass):
    '''return the cyclic spectrum of a given peptide'''
    #generate the linear peptide mass in peptide, eg NKEL,get N,NK,NKE,NKEL
    prefix_mass=[]
    prefix_mass.append(0)
    for i in range(0,len(peptide)):
        for j in alphabet:
            if j == peptide[i]:
                prefix_mass.append(prefix_mass[i]+int(aa_integer_mass[j][0]))
    peptide_mass=prefix_mass[len(peptide)]

    Cyclic_Spectrum=[]
    Cyclic_Spectrum.append(0)
    for i in range(len(peptide)):
        for j in range(i+1,len(peptide)+1):
            Cyclic_Spectrum.append(prefix_mass[j]-prefix_mass[i])
            if i>0 and j<len(peptide):
                Cyclic_Spectrum.append(peptide_mass-(prefix_mass[j]-prefix_mass[i]))
    return sorted(list(Cyclic_Spectrum))

def consistent(list1,list2):
    '''judge whether two given lists are consistent nor not
    consistent not only means that the characters are going to be same in two lists
    but also the number of specific characters are same two lists '''
    list3=list2[:]
    for i in list1:
        if i in list3:
            list3.remove(i)
        else:
            return False

def CyclopeptideSequencing(Spectrum):
    '''use the branch-and-bound algorithm to generate the cyclic peptide from given spectrum'''
    Final_peptides=[]
    candidate_peptides=[""]
    while len(candidate_peptides)!=0:
        candidate_peptides=Expand(candidate_peptides)
        for peptide_key in list(candidate_peptides.keys()):
            peptide_mass=candidate_peptides[peptide_key]
            peptide_mass_sum=sum(peptide_mass)
            if peptide_mass_sum == Spectrum[-1]:
                if cyclic_spectrum(peptide_key,alphabet,aa_integer_mass)==Spectrum and (peptide_mass not in Final_peptides):
                    Final_peptides.append(peptide_mass)
                else:
                    del candidate_peptides[peptide_key]
            elif peptide_mass_sum not in Spectrum:
                del candidate_peptides[peptide_key]
            elif consistent(peptide_mass,Spectrum)==False:
                del candidate_peptides[peptide_key]
    return Final_peptides

Spectrum=[0,113,128,186,241,299,314,427]
'''
with open("dataset_369294_6.txt",'r') as ff:
    for line in ff.readlines():
        Spectrum.extend([int(i) for i in line.split()])
'''
a=CyclopeptideSequencing(Spectrum)
for i in a:
    print('-'.join([str(j) for j in i]))

