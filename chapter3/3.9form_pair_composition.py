def format_k_d_composition(text,k,d):
    composition=[]
    for i in range(len(text)-d-k-2):
        first=text[i:i+k]
        last=text[i+k+d:i+d+k+k]
        a=first+"|"+last
        composition.append(a)
    return composition

text='TAATGCCATGGGATGTT'
k=3
d=2

a=format_k_d_composition(text,k,d)
final=[]
for i in a:
    b='('+i+')'
    final.append(b)

final=sorted(final)
print(''.join(final))