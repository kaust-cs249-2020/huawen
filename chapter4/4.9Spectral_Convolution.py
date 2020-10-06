def Spectral_Convolution(spectrum):
    '''The list of elements in the convolution of Spectrum. 
    If an element has multiplicity k, it should appear exactly k times
    '''
    result=[]
    for i in range(len(spectrum)):
        for j in range(len(spectrum)):
            k=spectrum[j]-spectrum[i]
            if k>0:
                result.append(k)
    return result

spectrum=[0,137,186,323]
'''
with open("dataset_369297_4.txt",'r') as ff:
    for line in ff.readlines():
        spectrum.extend([int(i) for i in line.split()])
'''
a=Spectral_Convolution(spectrum)
print(" ".join(str(i) for i in a))