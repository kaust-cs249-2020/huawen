def Binary_String(k):
    '''for a given k,return all the bonary kmers'''
    letter=['0','1']
    final=[]
    if k==0:
        return letter
    elif k==1:
        return letter
    else:
        for i in Binary_String(k-1):
            for j in letter:
                item=i+j
                final.append(item)
    return final

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

def eulerian_cycle(graph):
    '''return the euler cycle from the adjacency list of dircted graph'''
    cycle=[]
    start=list(graph.keys())[0]
    cycle.append(start)
    edge_sum=sum((len(i) for i in graph.values()))
    while len(cycle)<(edge_sum+1):
        while graph.get(start):
            end=graph[start][0]
            cycle.append(end)
            graph[start].remove(end)
            start=cycle[-1]

        #对cycle重排,rearrange the order of the cycle,
        # make the node with still other outdegree as first one to start
        for i in cycle:
            if graph.get(i):
                index=cycle.index(i)
                cycle_new=[]
                cycle_new.extend(cycle[index:])
                cycle_new.extend(cycle[1:index])
                cycle_new.append(i)
        cycle=cycle_new
        start=cycle[-1]
    return cycle


def String_Spelled_by_a_Genome_Path(dnas):
    '''for given kmer overlap dnas, glue them together'''
    final_string=dnas[0]
    n=len(dnas)
    k=len(dnas[0])

    #dnas=sorted(dnas)
    for i in range(1,n):
       final_string += dnas[i][-1]

    return final_string

def k_universal_circular_string(k):
    '''return the cycle of k-universal string'''
    Patterns=Binary_String(k)
    dB=bruijn_graph_from_kmer(Patterns)
    path=eulerian_cycle(dB)
    string=String_Spelled_by_a_Genome_Path(path)
    a=pow(2,k) #the length of the kuniversal string is pow(2,k)-1 
    return string[:a]

print(k_universal_circular_string(8))
