mesa=[0,0,0]
pedido=[40,50,20]
x=1

while x!='3':
    print("Sistema de pedidos\n")
    print("1- Lançar Pedido")
    print("2- Fechar Conta")
    print("3- Encerrar Aplicativo")
    x=input("Escolha a opção :")
if x =='1':
     m=int(input("Qual mesa realizou o pedido?"))
     p=int(input("Qual o numero do pedido?"))
     mesa[m]=mesa[m]+pedido[p]
elif x=='2':
     m=int(input("Deseja encerrar a conta de qualk mesa?"))
     print("O valor total da conta",mesa[m]*1.1)
     n=u=int(input("Deseja que o serviço seja divido pra quantos pagantes?"))
     print("O valor por pessoa é R$",mesa[m]*1.1/n)
     mesa[m]=0
     print("Conta da mesa",m,"zerada")

