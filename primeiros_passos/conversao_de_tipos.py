preco = 10.30
print(preco)

# convertendo explicitamente com um construtor
preco = int(preco)
print(preco)

# convertendo implicitamente com uma operação de divisão
preco = preco / 2
print(preco)

preco = 10
print(preco // 3) # preserva o tipo inteiro

# convertendo números de strings
preco = "22.50"
print(float(preco))

idade = "18"
print(int(idade))

# convertendo números em strings
preco = 10.5
preco_str = str(preco)
print(f'preco: {type( preco )}')
print(f'preco_str: {type(preco_str)}')

idade = 18
idade_str = str(idade)
print(f'idade: {type( idade )}')
print(f'idade_str: {type(idade_str)}')
