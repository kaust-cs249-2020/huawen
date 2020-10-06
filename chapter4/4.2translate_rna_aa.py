RNA_codon={}

with open('RNA_codon_table_1.txt', 'r') as f1:
    for ip in f1.readlines():
        if ip != None:
            ip=ip.replace(" ",",")
            ip=ip.replace("\n","")
            ip=ip.split(",")
            for i in range(len(ip)):
                RNA_codon[ip[0]]=ip[1]
           

def translate_rna_aa(rna):
    '''translate the rna into an amino acid string Peptide'''
    aa=[]
    first_codon=rna[0:3]
    aa.append(RNA_codon[first_codon])
    i=3
    while aa[-1]!='':
        codon=rna[i:i+3]
        aa.append(RNA_codon[codon])
        i=i+3
    else:
        return ''.join(aa)

rna="AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
print(translate_rna_aa(rna))
