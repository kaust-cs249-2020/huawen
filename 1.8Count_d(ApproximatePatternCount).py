def Count_d(Pattern,Text,d):
    '''return the appear times of a pattern with at most d mismatich in a Text''' 
    L=len(Pattern)
    count=0
    for i in range(len(Text) - L + 1):
        compare_string=Text[i:i+L]
        distance=0
        for j in range(len(Pattern)):
            if Pattern[j] != compare_string[j]:
                distance+=1
        if distance <= d:
            count += 1
    return count

