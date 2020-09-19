def Approximate_Pattern_Match(Pattern,Text,d):
    '''return the positions of approximate pattern in text with at most d mismatches'''
    L=len(Pattern)
    approximate_pattern_first_position=[]
    for i in range(len(Text) - L+1):
        compare_string=Text[i:i+L]
        distance=0
        for j in range(len(Pattern)):
            if Pattern[j] != compare_string[j]:
                distance+=1
        if distance <= d:
            approximate_pattern_first_position.append(i)

    for item in approximate_pattern_first_position:
        print(item,end=" ")

