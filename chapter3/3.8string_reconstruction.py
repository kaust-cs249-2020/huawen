def bruijn_graph_from_kmer(patterns):
    '''return the de bruijn graph of the kmer patterns'''
    prefixs=[]
    final_output = {}
    for pattern in patterns:
        prefix=pattern[:-1]
        prefixs.append(prefix)
        suffix=pattern[1:]

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
    start=degree_calculator(graph) ##start from the node with the most outdegree
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
    dB=bruijn_graph_from_kmer(Patterns)
    path=eulerian_path(dB)
    final_string=String_Spelled_by_a_Genome_Path(path)
    return final_string

data=[]

with open('dataset_369273_7.txt', 'r') as f1:
    for ip in f1.readlines():
        if ip != None:
            # 从文件中读取行数据时，会带换行符，使用strip函数去掉 换行符后存入列表
            data.append(ip.strip("\n"))
            
a=string_reconstruction(25,data)
print(a)