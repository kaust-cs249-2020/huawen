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

def degree_calculator_v2(graph):
    '''for a given graph which is a dictionary represent the edges in graph,
    calculate each node's outdgree and indegree as a list
    '''
    node_degree={}
    for key,value in graph.items():
        node_degree[key]=[len(value),0]
    for value in graph.values():
        for i in value:
            if i in node_degree.keys():
                node_degree[i][1]+=1
            else:
                node_degree[i]=[0,1]
    return node_degree

def maximal_nonbranching_paths(graph):
    '''return the nonbranching paths in the graph'''
    paths=[]
    node_degree=degree_calculator_v2(graph)
    for node,connect_node in graph.items():
        if node_degree[node]!=[1,1]: #for the node which is not a 1-in-1-out node
            if node_degree[node][0]>0: # for the node which outdegree is more than 1
                for w in connect_node:
                    nonbranching_path=[]
                    nonbranching_path.append(node)
                    nonbranching_path.append(w)
                    while True:
                        a=nonbranching_path[-1] 
                        if node_degree[a]==[1,1]: #if the last node is a 1-in-1-out node,then add its connected node to the path
                            nonbranching_path.append(graph[a][0])
                        else:
                            break
                        #print(nonbranching_path)
                    paths.append(nonbranching_path)
    
        if node_degree[node]==[1,1]: #find out the isolated cycle
            #print(node)
            path=[]
            path.append(node)
            path.append(connect_node[0])
            while path[0]!=path[-1]:
                start=path[-1]
                if graph.get(start):
                    path.append(graph[start][0])
                else:
                    break
            if path[0]==path[-1]:
                paths.append(path)
                graph[path[-1]].remove(graph[path[-1]][0]) #remove one element from the cycle, ensure the same cycle appear once
    return paths

def String_Spelled_by_a_Genome_Path(dnas):
    '''for given kmer overlap dnas, glue them together'''
    final_string=dnas[0]
    n=len(dnas)
    k=len(dnas[0])

    #dnas=sorted(dnas)
    for i in range(1,n):
       final_string += dnas[i][-1]

    return final_string


def contig_generation(patterns):
    '''from the kmer patterns,generate the contig from their de bruijn graph
    contig is the nonbranching path in the de bruijn graph
    '''
    graph=bruijn_graph_from_kmer(patterns)
    a=maximal_nonbranching_paths(graph)
    final_contig=[]
    for i in a:
        final_contig.append(String_Spelled_by_a_Genome_Path(i))
    return final_contig

patterns=[]

with open('test.txt', 'r') as f1:
    for ip in f1.readlines():
        if ip != None:
            # 从文件中读取行数据时，会带换行符，使用strip函数去掉 换行符后存入列表
            patterns.append(ip.strip("\n"))

a=contig_generation(patterns)
for i in a:
    print(''.join(i))