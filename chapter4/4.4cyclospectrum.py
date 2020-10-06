aa_integer_mass={}
with open('integer_mass_table.txt', 'r') as f1:
    for ip in f1.readlines():
        if ip != None:
            ip=ip.replace(" ",",")
            ip=ip.replace("\n","")
            ip=ip.split(",")
            for i in range(len(ip)):
                aa_integer_mass[ip[0]]=ip[1]
#print(aa_integer_mass)
alphabet=list(aa_integer_mass.keys())

def cyclic_spectrum(peptide,alphabet,aa_integer_mass):
    ''' Generate the theoretical spectrum of a cyclic peptide'''
    #get linear aa's mass in the peptide,eg NQEL,get the mass of N,NQ,NQE,NQEL
    prefix_mass=[]
    prefix_mass.append(0)
    for i in range(0,len(peptide)):
        for j in alphabet:
            if j == peptide[i]:
                prefix_mass.append(prefix_mass[i]+int(aa_integer_mass[j]))
    peptide_mass=prefix_mass[len(peptide)]
    #print(prefix_mass)
    #print(peptide_mass)
    Cyclic_Spectrum=[]
    Cyclic_Spectrum.append(0)
    for i in range(len(peptide)):
        for j in range(i+1,len(peptide)+1):
            Cyclic_Spectrum.append(prefix_mass[j]-prefix_mass[i])
            if i>0 and j<len(peptide):
                Cyclic_Spectrum.append(peptide_mass-(prefix_mass[j]-prefix_mass[i]))
    return sorted(list(Cyclic_Spectrum))

a=cyclic_spectrum("NQEL",alphabet,aa_integer_mass)
print(a)
for i in a:
    print(i,end=" ")