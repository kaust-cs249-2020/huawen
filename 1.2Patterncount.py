def PatternCount(Text,Pattern):
    '''count certain given pattern in a text'''
    count=0
    i=0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)]==Pattern:
            count=count+1
    return count
            
    
