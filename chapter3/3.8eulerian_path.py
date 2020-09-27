#读取文件,read file
data=[]
with open("aaa.txt",'r') as ff:
    for line in ff.readlines():
        line=line.replace(" -> ",',')
        line=line.replace("\n",'')
        line=line.split(',')
        data.append(line)

#将文件内容做成字典，一键多值，键代表起点，值代表终点,transfer the data into dictionary
data_input={}
for i in data:
    data_input[i[0]]=i[1:]
#print(data_input)

def degree_calculator(graph):
    '''for a given graph which is a dictionary represent the edges in graph,
    calculate each node's degree,indgree puls 1,outdgree minus 1
    return the node with the min degrees which smaller than 0
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


a=eulerian_path(data_input)
#print(a)
print('->'.join(a))
