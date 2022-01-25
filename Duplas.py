# tuplas são criadas e  nao podem ser  modificadas em execução

dimensoes = (200,50,30,58,70)
print(dimensoes[0])
print(dimensoes[1])
print("percorrendo os elementos da tupla: ")
for dimensao in dimensoes:
    print(dimensao)
print("conteudo t1")
t1 = (1,)
print(t1[0])