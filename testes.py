f = open("InfoCursos\\ESMAD\\1.txt","r", encoding='utf-8')
Textos=[]
for l in f:
    a = l
    Textos.append(a)

f.close()

print(Textos[0])
print(Textos[1])
