
def FrequencyTable(Text,k):
    freqMap={}
    n=len(Text)
    for i in range(n-k):
        Pattern=Text[i:i+k]
        if Pattern not in freqMap.keys():
            freqMap[Pattern]=1
        else:
            freqMap[Pattern]=freqMap[Pattern]+1
    return freqMap

def BetterFrequentWords(Text,k):
    freqMap=FrequencyTable(Text,k)
    MaxMap=[]
    for key,value in freqMap.items():
        if value == max(freqMap.values()):
            MaxMap.append(key)
    return MaxMap

def FindClumps(Text,k,L,t):
    n=len(Text)
    Patterns=[]
    Final_Patterns=[]
    for i in range(n-L):
        Window=Text[i:L+i]
        freMap=FrequencyTable(Window,k)
        for key,value in freMap.items():
            if value >= t:
                Patterns.append(key)
    return set(Patterns)

    '''
    for item in Patterns:
        if item not in Final_Patterns:
            Final_Patterns.append(item)
            print(item)
    '''


