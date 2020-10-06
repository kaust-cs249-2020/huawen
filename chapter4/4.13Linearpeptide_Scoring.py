spectrum=[0,99,113,114,128,227,257,299,355,356,370,371,484]
'''
with open("dataset_369301_1.txt",'r') as ff:
    for line in ff.readlines():
        spectrum.extend([int(i) for i in line.split()])
'''
peptide="NQEL"

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
    '''generate the linear spectrum of a peptide 
    peptide is a string'''
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

def Linearpeptide_Scoring(Peptide, Spectrum):
    '''score the spectrum and the ideal linear spectrum of peptide'''
    peptide_mass=linear_spectrum(Peptide,alphabet,aa_integer_mass)
    score=0
    spectrum=Spectrum[:]
    for i in peptide_mass:
        if i in spectrum:
            score+=1
            spectrum.remove(i)
    return score

print(Linearpeptide_Scoring(peptide,spectrum))