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
    '''return the all of the nonbranching paths in the graph'''
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

#读取文件, read data
data=[]
with open("test.txt",'r') as ff:
    for line in ff.readlines():
        line=line.replace(" -> ",',')
        line=line.replace("\n",'')
        line=line.split(',')
        data.append(line)

#将文件内容做成字典，一键多值，键代表起点，值代表终点, transfer the data to dictionary
data_input={}
for i in data:
    data_input[i[0]]=i[1:]


a=maximal_nonbranching_paths(data_input)
for i in a:
    print(' -> '.join(i))