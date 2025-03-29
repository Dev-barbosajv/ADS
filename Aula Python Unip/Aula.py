#tipicamos variaveis, processamos variaveis e decisao com variaveis.
#Foi feito um input buscando P1, P2, PIM e media da nota // media = ( P1 * 0.4 ) + ( P2 * 0.4 ) + ( PIM * 0.2 )
#se a media > 5 : aprovado
#se media < 7 >= 5 : exame
#se media <5 : reprovado

#if ( media > 7)
#print ( "aluno aprovado" )
#elif ( " media < 7 " )
#print ( "aluno de exame " )
#else 
#print ("aluno retido")
#return 0

#while busca em sequencia varios resultados ( dentro de uma condição ) que foi solicitada.
#no esquema de estrutura de repetição, tem que ter uma ideia que faça tenha um termino que no caso será utilizado a palavra "Para" ou "for" ( utilizada para executar um numero x de comandos simultaneos )

#exemplo:
#start = 0;
#stop = 10;
#step = 2;

#for i in range ( start, stop, step):
#   print(i);


#Exercicio

# Solicita ao usuário o número inicial e o número final da tabuada
#sstart = int(input("Qual o número inicial da tabuada? "))
#stop = int(input("Qual o número final da tabuada? "))
#tabuada = int(input("Multiplicado por: "))

# Gera a tabuada para o intervalo especificado
#print(f"\nTabuada de {tabuada} do {start} ao {stop}:\n")
#for i in range(start, stop + 1):  # Inclui o número final no intervalo
#    calculo = i * tabuada
#    print(f"{i} x {tabuada} = {calculo}")


#valor = 0
#resultado = 0
#i = 0

#valor = int ( input ("Digite um valor de 2 a 10 para o calulo da tabuada"))
# for i in range ( 1, 11, 1)
#   resultado = valor * 1  
#print ("O resultado é". resultado)

# Algoritimo para executar uma tabela e filtra entre impares e pares.
start = int(input("Qual o número inicial da tabuada? "))
stop = int(input("Qual o número final da tabuada? "))
tabuada = int(input("Multiplicado por: "))


filtro = input("Deseja filtrar por 'pares', 'impares' ou 'todos'? ").strip().lower()


print(f"\nTabuada de {tabuada} do {start} ao {stop}:\n")
for i in range(start, stop + 1):  
    if filtro == "pares" and i % 2 != 0:
        continue  #
    elif filtro == "impares" and i % 2 == 0:
        continue  

    calculo = i * tabuada
    print(f"{i} x {tabuada} = {calculo}")
