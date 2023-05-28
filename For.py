for variavel in range(10):
    print(variavel)

for variavel in range (1,10): 
    print(variavel)

# 1, 4, 7, 10
"""nota1 = float(input('informe sua nota 1 : '))
nota2 = float(input('informe sua nota 2: '))"""

soma = 0

for i in range (1,4):
    nota = float(input(f'informe a sua nota {i}: '))

    soma = soma + nota

print(soma/ 3)