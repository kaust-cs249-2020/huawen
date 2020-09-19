def Pattern_match_position(Text,Pattern):
    '''find out the pattern's location on genes'''
    position=[]
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            position.append(i)
    for item in position:
        print(item,end=" ")

