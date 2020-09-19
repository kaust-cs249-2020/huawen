
def FrequencyTable(Text,k):
    freqMap={}
    n=len(Text)
    for i in range(n-k+1):
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
