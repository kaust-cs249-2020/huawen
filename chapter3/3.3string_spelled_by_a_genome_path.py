def String_Spelled_by_a_Genome_Path(dnas):
    '''generate the geneme from the overlap kmers'''
    final_string=dnas[0]
    n=len(dnas)
    k=len(dnas[0])
    #dnas=sorted(dnas)
    for i in range(1,n):
       final_string += dnas[i][-1]
    return final_string

dnas=["ACCGA","CCGAA","CGAAG","GAAGC","AAGCT"]
print(String_Spelled_by_a_Genome_Path(dnas))

data=[]
with open('dataset_369268_3.txt', 'r') as f1:
    for ip in f1.readlines():
        if ip != None:
            # 从文件中读取行数据时，会带换行符，使用strip函数去掉 换行符后存入列表
            data.append(ip.strip("\n"))

String_Spelled_by_a_Genome_Path(data)
