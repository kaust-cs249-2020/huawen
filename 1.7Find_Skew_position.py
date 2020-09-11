def Minimum_Skew(Text):
    '''return the position in a genome where
    the skew diagram attains a minimum'''
    Skew={0:0}
    skew=0
    for i in range(len(Text)):
        if Text[i]=="G":
            skew += 1
            Skew[i+1]=skew
        elif Text[i]=="C":
            skew -= 1
            Skew[i+1]=skew
        else:
            Skew[i+1]=skew

    Skew_min = min(Skew.values())
    min_skew_position=[]

    for position,value in Skew.items():
        if value == Skew_min:
            min_skew_position.append(position)

    for j in min_skew_position:
        print(j,end=" ")
