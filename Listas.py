# > Listas

#antes

nota1 = 7,9
nota2 = 9,7
nota3 = 8.2

# Com lista

notas = { 7,9, 9,7, 8,2}

# CRIANDO LISTAS 
 
lista = []
lista = list
lista = 25, ' jaiane', 3,1415, True

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])


# MÉTODOS DE LISTAS

lista = [1, 3, 12, 8, 2]

# append

print(lista)

lista.append(3)

print('depois do append:', lista)

# insert

lista.insert(2, 10)

print('depois do insert:', lista)

# lista

lista.pop()
print('lista após o pop:', lista)

# Remove

lista.remove(3)

print('depois do remove:', lista)

# COUNT 

print('quantidade de 2 na lista:', lista.count(2))

#indez

print('indice do elemento 12:', lista.index(12))

# SURT

lista.sort(reverse=True)

print(lista)

# FUNÇÕES DE LISTAS

print(len(lista))

#SUM

print(sum(lista))

#MAX 

print('maior elemento da lista:', max(lista))

#MIN

print('menor elemento da lista:', min(lista))
