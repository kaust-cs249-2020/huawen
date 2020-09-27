import random

def string_composition(k,text):
  '''generate the kmer in the text'''
  kmer_pattern=[]
  for i in range(len(text)-k+1):
      pattern=text[i:i+k]
      kmer_pattern.append(pattern)
  random.shuffle(kmer_pattern)
  return kmer_pattern

def text_save(filename, data):#filename为写入CSV文件的路径，data为要写入数据列表.
  file = open(filename,'a')
  for i in range(len(data)):
    s = str(data[i]).replace('[','').replace(']','')#去除[],这两行按数据不同，可以选择
    s = s.replace("'",'').replace(',','') +'\n'  #去除单引号，逗号，每行末尾追加换行符
    file.write(s)
  file.close()
  print("保存文件成功")

a=string_composition(5,"CAATCCAAC")
print(a)