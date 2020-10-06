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

#print(cyclic_spectrum("NQEL",alphabet,aa_integer_mass))

def Cyclopeptide_Scoring(Peptide, Spectrum):
    '''generate the cyclic spectrum of the peptide
    and calculate the scores between cyclic spectrum and spectrum'''
    peptide_mass=cyclic_spectrum(Peptide,alphabet,aa_integer_mass)
    score=0
    spectrum=Spectrum[:]
    for i in peptide_mass:
        if i in spectrum:
            score+=1
            spectrum.remove(i)
    return score

Spectrum=[]
with open("dataset_369295_3.txt",'r') as ff:
    for line in ff.readlines():
        Spectrum.extend([int(i) for i in line.split()])

print(Cyclopeptide_Scoring("VGCRWTVALLIGTNNPCGWATGKLQIFNPYIGAPIWVTLTRFRPSKHTP",Spectrum))
