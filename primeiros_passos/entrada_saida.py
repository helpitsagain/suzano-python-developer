# print()
# https://docs.python.org/3/library/functions.html#print
nome = "Lucas"
sobrenome = "Michels"

print(nome, sobrenome)
print(nome, sobrenome, end='...')
print(nome, sobrenome, end='!\n')
print(nome, sobrenome, sep='_')

# input()
# https://docs.python.org/3/library/functions.html#input
nome = input("Informe seu nome: ")
idade = input("Informe sua idade: ")

print(f"Seu nome é {nome} e você tem {idade} anos!")

