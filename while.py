numero_sorteado = 15

numero_escolhido = int(input('informe um número entre 1 e 20: '))

while numero_escolhido != numero_sorteado:
    print('você errou o número, tente novamente...')

    numero_escolhido = int(input('informe um número entre 1 e 20: '))

# Exemplo 02: Estrutura com contador

contador = 0

while contador < 5:
    print(contador)

    contador = contador + 1