def string_spelled_by_gapped_patterns(k,d,gapped_patterns):
    '''gapped_patterns is the kmer pair patterns,between them is the strings which length is d
    this function is going to glue these pair patterns
    '''
    data_all=[]
    first_pattern=[]
    second_pattern=[]

    for i in gapped_patterns:
        i=i.split('|',1)
        data_all.append(i)

    for i in data_all:
        first_pattern.append(i[0])
        second_pattern.append(i[1])
        
    prefix_string=first_pattern[0]
    suffix_string=second_pattern[0]
    
    for i in range(len(first_pattern)-1):
        if first_pattern[i][1:]==first_pattern[i+1][:-1]:
            prefix_string+=(first_pattern[i+1][-1])

    for i in range(len(second_pattern)-1):
        if second_pattern[i][1:]==second_pattern[i+1][:-1]:
            suffix_string+=(second_pattern[i+1][-1])
    
    for i in range(k+d,len(prefix_string)):
        if prefix_string[i] !=suffix_string[i-k-d]:
            return "there is no string spelled by the gapped patterns" 
    
    return prefix_string+suffix_string[-(k+d):]   


gapped_patterns=[]

with open('dataset_369278_4.txt', 'r') as f1:
    for ip in f1.readlines():
        if ip != None:
            # 从文件中读取行数据时，会带换行符，使用strip函数去掉 换行符后存入列表
            gapped_patterns.append(ip.strip("\n"))

#print(gapped_patterns)
print(string_spelled_by_gapped_patterns(4,2,gapped_patterns))