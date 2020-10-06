aa_integer_mass={}
with open('integer_mass_table.txt', 'r') as f1:
    for ip in f1.readlines():
        if ip != None:
            ip=ip.replace(" ",",")
            ip=ip.replace("\n","")
            ip=ip.split(",")
            for i in range(len(ip)):
                aa_integer_mass[ip[0]]=ip[1]

alphabet=list(aa_integer_mass.keys())
#print(alphabet)

def linear_spectrum(peptide,alphabet,aa_integer_mass):
    '''generate the linear spectrum of a peptide 
    peptide is a string'''
    prefix_mass=[]
    prefix_mass.append(0)
    for i in range(0,len(peptide)):
        for j in alphabet:
            if j == peptide[i]:
                prefix_mass.append(prefix_mass[i]+int(aa_integer_mass[j]))
    Linear_spectrum=[0]
    for i in range(len(peptide)):
        for j in range(i+1,len(peptide)+1):
            Linear_spectrum.append(prefix_mass[j]-prefix_mass[i])
            #print(i,j)
            #print(Linear_spectrum)
    return sorted(list(Linear_spectrum))
    
a=linear_spectrum("NQEL",alphabet,aa_integer_mass)
for i in a:
    print(i,end=" ")

