from collections import defaultdict

def overlap_graph(dnas):
    '''return the overlap graph in the form of
    an adjacency list'''
    final_output=defaultdict(list)
    k=len(dnas[0])
    for i in range(len(dnas)):
        for j in range(len(dnas)):
            if dnas[i][1:]==dnas[j][:-1]:
                final_output[dnas[i]].append(dnas[j])
    return final_output

dnas=[]
with open('dataset_369268_11.txt', 'r') as f1:
    for ip in f1.readlines():
        if ip != None:
            # 从文件中读取行数据时，会带换行符，使用strip函数去掉 换行符后存入列表
            dnas.append(ip.strip("\n"))
            
final_output=overlap_graph(dnas)

file=open("result1.txt","w")
for k,v in final_output.items():
	file.write(str(k)+' -> '+",".join(v)+'\n')
file.close()
print("保存文件成功")
