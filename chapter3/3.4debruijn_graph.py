def DeBruijn_Graph(k,text):
    '''for a given text and k,return all the kmers in text,
    and their adjacencey list of de bruijn graph'''

    final_output = {}
    edges = []
    for i in range(len(text)-k+1):
        edge = text[i:i+k]
        edges.append(edge)
        
    for j in range(len(edges)):
        prefix=edges[j][:-1]
        suffix=edges[j][1:]
        if final_output.get(prefix):
            final_output[prefix].append(suffix)
        else:
            final_output[prefix]=[suffix]
    return final_output

dnas="AAGATTCTCTAAGA"
            
final_output=DeBruijn_Graph(4,dnas)

file=open("result1111.txt","w")
for k,v in final_output.items():
	file.write(str(k)+' -> '+",".join(v)+'\n')
file.close()
print("保存文件成功")
