c1 = 0
c2 = 0
c3 = 0

numero_eleitores = int(input("Digite o número de eleitores: "))

for i in range(numero_eleitores):
    print("Eleitor ", i + 1, " (faltam ", numero_eleitores - i, ")")
    votos = input("Escolha entre o c1, c2, c3 :")
if votos == c1:
   c1 = c1+1
if votos == c2:
    c2 = c2+1
if votos == c3:
 c3 = c3+1

print("O Candidato 1 teve ",c1, "votos")
print("O Candidato 2 teve ",c2, "votos")
print("O Candidato 3 teve ",c3, "votos")
