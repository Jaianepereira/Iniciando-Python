# > ESTRUTURA CONDICIONAIS

idade = 10

if idade >= 18:
    print('você é maior de idade.')
else:
    print('você é menor de idade.')
     


"""

Imagine que você queira imprimir "Aprovada", caso o estudante tenha uma média superior ou igual a 7, e "Reprovado", caso a média seja inferior a 7.

"""
media = float(input('informe a média do estudante'))

if media >= 7:
    print('você foi aprovada(o)!')
elif media >= 5:
    print('recuperação')
else: 
    print('você foi reprovada(o).')
