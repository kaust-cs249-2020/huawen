'''
DeBruijn(Patterns)
    dB ← graph in which every k-mer in Patterns is isolated edge between its prefix and suffix
    dB ← graph resulting from gluing all nodes in dB with identical labels
    return dB
'''

def bruijn_graph_from_kmer(patterns):
    '''for given kmer patterns,generate the de bruijn graph of these patterns'''
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

patterns=[]

with open('dataset_369270_8.txt', 'r') as f1:
    for ip in f1.readlines():
        if ip != None:
            # 从文件中读取行数据时，会带换行符，使用strip函数去掉 换行符后存入列表
            patterns.append(ip.strip("\n"))
            
final_output=bruijn_graph_from_kmer(patterns)

file=open("result1.txt","w")
for k,v in final_output.items():
	file.write(str(k)+' -> '+",".join(v)+'\n')

file.close()
print("保存文件成功")
