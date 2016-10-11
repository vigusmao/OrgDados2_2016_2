from random import randint
from time import time

MAX_ELEMENTO = 10**9
N = 640000



def criar_lista(tamanho):
    conjunto = set()
    while len(conjunto) < tamanho:
        novo = randint(1, MAX_ELEMENTO)
        conjunto.add(novo)
    return list(conjunto)


def intersecao_quadratico(lista1, lista2):
    ''' Retorna uma lista contendo a intersecao das duas listas
        Tempo O(n*m), onde n e m sao os tamanhos das listas
    '''
    resultado = []
    for elemento in lista1:
        for candidato in lista2:
            if candidato == elemento:
                resultado.append(elemento)
                break
    return resultado

def intersecao_busca_binaria(lista1, lista2):
    ''' Retorna uma lista contendo a intersecao das duas listas
        Tempo O(n log m), onde n eh o tamanho da menor lista
        e m eh o tamanho da maior lista.
    '''
    resultado = []
    
    maior_lista = lista1
    menor_lista = lista2
    if len(menor_lista) > len(maior_lista):
        menor_lista, maior_lista = maior_lista, menor_lista

    menor_lista_ordenada = sorted(menor_lista)
    
    for elemento in maior_lista:
        if busca_binaria(menor_lista_ordenada, elemento) > -1:
            resultado.append(elemento)

    return resultado

def intersecao_hashing(lista1, lista2):
    ''' Retorna uma lista contendo a intersecao das duas listas
        Tempo O(n), onde n eh o tamanho da maior lista.
    '''
    resultado = []

    conjunto1 = set()
    for elemento in lista1:
        conjunto1.add(elemento)

    for candidato in lista2:
        if candidato in conjunto1:
            resultado.append(candidato)

    return resultado
    

def busca_binaria(lista, x):
    ''' Retorna o indice de x na lista ORDENADA dada;
        -1 se nao encontrou
    '''
    inicio = 0
    fim = len(lista) - 1
    while inicio <= fim:
        posicao_central = (inicio + fim) // 2
        elemento_central = lista[posicao_central]
        if elemento_central == x:
            return posicao_central
        if elemento_central < x:
            inicio = posicao_central + 1
        else:
            fim = posicao_central - 1
    return -1
    


lista1 = criar_lista(N)
lista2 = criar_lista(N)

##start = time()
##intersecao = intersecao_quadratico(lista1, lista2)
##duracao = time() - start
##print("\nquadratico\ntamanho = %d -- duracao: %f segundos" %
##      (len(intersecao), duracao))

start = time()
intersecao = intersecao_busca_binaria(lista1, lista2)
duracao = time() - start
print("\nbusca binaria\ntamanho = %d -- duracao: %f segundos" %
      (len(intersecao), duracao))

start = time()
intersecao = intersecao_hashing(lista1, lista2)
duracao = time() - start
print("\nhashing\ntamanho = %d -- duracao: %f segundos" %
      (len(intersecao), duracao))




