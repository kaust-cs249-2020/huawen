import 1.2Patterncount.py

def FrequentWords(Text,k):
    '''find the most frequent k-mer in text'''
    FrequentPatterns=[]
    Count=[]
    Final_frequentpatterns=[]
    for i in range(len(Text)-k):
        Pattern=Text[i:k+i]
        Count.append(PatternCount(Text,Pattern))
    maxCount=max(Count)
    for i in range(len(Text)-k):
        if Count[i]==maxCount:
            FrequentPatterns.append(Text[i:k+i])
            
    '''remove the deplicates in the FrequentPatterns'''
    for id in FrequentPatterns:
        if id not in Final_frequentpatterns:
            Final_frequentpatterns.append(id)
    for item in Final_frequentpatterns:
        print(item)


'''improve vision of FrequentWords_imp'''
def FrequentWords_imp(Text,k):
    maxCount=0
    for i in range(len(Text)-k):
        Pattern=Text[i:i+k]
        Count=PatternCount(Text,Pattern)
        if Count>maxCount:
            maxCount=Count
            FrequentPatterns=[]
            FrequentPatterns.append(Pattern)
        elif Count == maxCount:
            FrequentPatterns.append(Pattern)
    print(set(FrequentPatterns))
            
        
