"""
Crie um exercício que receba 3 notas,calcule a média,e se for maior que 7.0 exibir a mensagem aprovado,se não reprovado

"""

num1=8
num2=10
num3=10
media=(num1+num2+num3)/3
if media >= 7:
    print(media)
    print("Aprovado")
else:
    print(media)
    print("Reprovado")

"""
Criar um algoritmo que exiba as seguintes mensagens de acordo com a media(3 notas e calculo da media0
0 - 4 reprovado
4.1 até 5.9 recuperação
 acima de 6 aprovado
 
 """
num1=8
num2=7
num3=4
media=(num1+num2+num3)/3
if media <= 4:
    print(media)
    print("Reprovado")

elif media > 6:
    print(media)
    print("Recuperação")

else:
    print(media)
    print("Aprovado")



