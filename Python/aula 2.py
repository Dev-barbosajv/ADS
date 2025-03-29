#nessa aula será focada a criação de textos.

email = "email@email.com"
faturamento = 1000
custo = 300 
lucro = faturamento - custo

print(f"Faturamento da empresa: {faturamento}, Custo:{custo}, Lucro: {lucro}") 

email_cliente = "emailcliente@email.com"


email_client = email_cliente.upper() # transforma tudo em maiuscula
print(email_client)
email_client = email_cliente.lower() # transforma tudo em minuscula
print(email_client)

# "@"
print(email_cliente.find("@")) # acha a posição do caracter @ na string. Quando não encontrar, ele irá mostrar -1

# pegar um caracter
print(email_cliente[2])

#tamanho da string
print(len(email_cliente))

#buscar no texto
print(email_cliente[13:18])

#trocar um pedaço do texto
novo_email = email_cliente.replace("email.com", "hotmail.com")
print(novo_email)

nome = "Joao Maria"

print(nome.capitalize())#deixa a primeira letra maiuscula
print(nome.title())#deixa a primeira letra de cada palavra maiuscula

#casos especiais de texto