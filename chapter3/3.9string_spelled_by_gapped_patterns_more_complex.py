def bruijn_graph_from_kmer_pairs(patterns):
    '''return the de bruijn graph of the kmer pair patterns'''
    prefixs=[]
    final_output = {}
    for pattern in patterns:
        prefix=(pattern[0][:-1],pattern[1][:-1])
        prefixs.append(prefix)
        suffix=(pattern[0][1:],pattern[1][1:])

        if final_output.get(prefix):
            final_output[prefix].append(suffix)
        else:
            final_output[prefix]=[suffix]
    return final_output

def degree_calculator(graph):
    '''for a given graph which is a dictionary represent the edges in graph,
    calculate each node's degree,indgree puls 1,outdgree minus 1
    return the node with the min degrees which less than 0
    '''
    node_degree={}
    for key,value in graph.items():
        node_degree[key]=(-1)*len(value)
    for value in graph.values():
        for i in value:
            if i in node_degree.keys():
                node_degree[i]+=1
            else:
                node_degree[i]=1
    return min(node_degree,key=node_degree.get)

def eulerian_path(graph):
    '''return the euler path from the adjacency list of dircted graph'''
    path=[]
    start=degree_calculator(graph) #start from the node with the most outdegree
    path.append(start)
    final_path=[]
    while len(path)!=0:
        new_start=path[-1]
        if graph.get(new_start):
            end=graph[new_start][0]
            path.append(end)
            graph[new_start].remove(end)
        else:
            final_path.append(path.pop())

    edge_sum=sum((len(i) for i in graph.values()))
    
    if edge_sum==0:
        return list(reversed(final_path))

    return ['no eulerian path']

def String_Spelled_by_a_Genome_Path(dnas):
    '''for given kmer overlap dnas, glue them together'''
    final_string=dnas[0]
    n=len(dnas)
    k=len(dnas[0])

    #dnas=sorted(dnas)
    for i in range(1,n):
       final_string += dnas[i][-1]

    return final_string

def string_reconstruction(k,Patterns):
    '''Patterns is a list of gernerated reads, 
    each pattern's length is k
    return the text with kmer composition equal to patterns
    '''
    dB=bruijn_graph_from_kmer_pairs(Patterns)
    path=eulerian_path(dB)
    final_string=String_Spelled_by_a_Genome_Path(path)
    return final_string

def string_spelled_by_gapped_patterns_more_complex(k,d,gapped_patterns):
    '''gapped_patterns is the kmer pair patterns,between them is the strings which length is d
    this function is going to glue these pair patterns
    '''
    data_all=[]
    first_pattern=[]
    second_pattern=[]

    for i in gapped_patterns:
        i=i.split('|',1)
        data_all.append(i)

    pattern_db=bruijn_graph_from_kmer_pairs(data_all) #generate the bruijn graph
    
    pattern_path=eulerian_path(pattern_db) #generate the euler path
    
    for pattern in pattern_path:
        first_pattern.append(pattern[0])
        second_pattern.append(pattern[1])

    prefix_string=String_Spelled_by_a_Genome_Path(first_pattern)
    suffix_string=String_Spelled_by_a_Genome_Path(second_pattern)

    for i in range(k+d+1,len(prefix_string)):
        if prefix_string[i] !=suffix_string[i-k-d]:
            return "there is no string spelled by the gapped patterns" 
    
    return prefix_string+suffix_string[-(k+d):]   


gapped_patterns=[]

with open('test.txt', 'r') as f1:
    for ip in f1.readlines():
        if ip != None:
            # 从文件中读取行数据时，会带换行符，使用strip函数去掉 换行符后存入列表
            gapped_patterns.append(ip.strip("\n"))

#print(gapped_patterns)
a=string_spelled_by_gapped_patterns_more_complex(4,200,gapped_patterns)
print(a)