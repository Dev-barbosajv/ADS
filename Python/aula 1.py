faturamento = 1200 #tipo: int -> numero inteiro
custo = 750.32 #tipo: float -> numero com casa decimal

novas_vendas = 100 #tipo: int -> numero inteiro
faturamento = faturamento + novas_vendas #calculo do faturamento

imposto = faturamento * 0.1 #10% de imposto
#calculo do imposto

lucro = faturamento - custo - imposto#calculo
margem_lucro = lucro / faturamento

print ( "Faturamento foi de", faturamento)
print ( "Custo foi de", custo)
print ( "Lucro foi de", lucro)
print ( "A Margem de lucro foi de ", round(margem_lucro, 3)) #round -> arredondar o valor

mensagem = "O Faturamento da loja foi de faturamento"
email = "emailqualquer@gmail.com" #tipo strin -> texto

teve_lucro = True #tipo: bool/boolean -> verdadeiro ou falso ( false ou true)

#mod -> % resto da divisão
print ( 10 % 3 ) #resto da divisão de 10 por 3
tempo_contrato = 170
tempo_anos = 170 / 12
print("tempo em anos", tempo_anos)
tempo_meses = 170 % 12
print("tempo em meses", tempo_meses)