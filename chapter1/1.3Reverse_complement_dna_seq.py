def Reverse_complement_dna_seq(Seq):
    '''get the reverse and complementary sequences of seq'''
    Seq=Seq[::-1]
    Seq_reverse=[]
    for i in range(len(Seq)):
        if Seq[i]=="A":
            Seq_reverse.append("T")
        elif Seq[i]=="T":
            Seq_reverse.append("A")
        elif Seq[i]=="C":
            Seq_reverse.append("G")
        elif Seq[i]=="G":
            Seq_reverse.append("C")
    Seq=''.join(Seq_reverse)
    print(Seq)

 
            
'''another methods to get the reverse complementary sequences
https://blog.csdn.net/lotusng/article/details/103315213'''
