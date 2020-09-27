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

print(data_input)

def eulerian_cycle(graph):
    '''return the euler cycle from the adjacency list of dircted graph'''
    cycle=[]
    start=list(graph.keys())[0]
    cycle.append(start)
    edge_sum=sum((len(i) for i in graph.values()))
    while len(cycle)<(edge_sum+1):  #the length of cycle(number of node) euqal to number of edges+1
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


a=eulerian_cycle(data_input)
print(a)
print('->'.join(a))
