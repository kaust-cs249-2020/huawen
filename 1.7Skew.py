def Skew(Text):
    '''return the value change of nucleotide G and C,initial number is 0,
    when it's G, plus 1,when it is C, minus 1'''
    skew = 0
    skew_all=[]
    skew_all.append(skew)
    for i in range(len(Text)):
        if Text[i]=="G":
            skew += 1
        elif Text[i]=="C":
            skew -= 1
        skew_all.append(skew)
    for j in skew_all:
        print(j,end=' ')

