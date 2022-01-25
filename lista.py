nomes=['Stephano','Marcos','Larissa','Raissa','Bruna','Jorge']
print(nomes)

# listar um unico elemento da lista

print(nomes[2])
print(nomes[-1])

idade=['22','12','21','30','32','15']
print(idade)
print("o aluno da posição 3 é o "+nomes[3]+"e a sua idade é:",idade[3])

moto=['Honda','Bmw','Yamaha']
print(moto)

# acrescentar valores a lista

moto.append('yamaha')
print(moto)
print(moto[2])

# inserir em posição determinada

fruta=['Banana','Maçã','Uva','Goiaba']
print(fruta)
fruta.insert(2,'sssa')

# deletar

del fruta[2]
print(fruta)
print("tamanho da lista: ",len(fruta))