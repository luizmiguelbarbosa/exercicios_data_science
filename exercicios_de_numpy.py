#exercicios numpy

#autor : Luiz Miguel

import numpy as np

#1 Criação de arrays
#1.1: Crie um array NumPy com os números de 0 a 9 
arrayseq = np.arange(0,10)
print(arrayseq)

#1.2: Crie um array de 10 zeros
arrayzero = np.zeros(10)
print(arrayzero)

#1.3: Crie um array de 10 uns
arrayum = np.ones(10)
print(arrayum)

#1.4: Crie um array com 10 números aleatórios entre 0 e 1
arrayrandom = np.random.uniform(0,1, 10)
print(arrayrandom)

#1.5: Crie um array de números inteiros de 50 a 100 (inclusive)
arrayint = np.arange(50,101)
print(arrayint)


#2 Operações com arrays
#2.1: Crie dois arrays de 10 elementos e faça:
#Soma
#Subtração
#Multiplicação
#Divisão

array1 = np.random.rand(10)
array2 = np.random.rand(10)

array3 = array1 + array2
array3 = array1 - array2
array3 = array1 * array2
array3 = array1/array2

#2.2 crie um array Numpy com 10 valores igualmente espaçados entre 5 e 15 
arrayespacado = np.linspace(5, 15, 10)
print(arrayespacado)

#2.3 dado o array abaixo, selecione apenas os números pares
arr = np.array([1,4,7,10,13,16])
pares = arr[arr%2==0]
print(pares)

#2.4 calcule a média, mediana e desvio padrão do arry abaixo
#média
arr2 = np.array([2,8,5,10,3])
media = np.mean(arr2)
#mediana
mediana = np.median(arr2)
#desvio padrão
desvio_padrao = np.std(arr2)

#2.5 faça a multiplacação matricial entre as matrizes
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

c = np.dot(a,b) #multiplicação matricial 

#2.6 criar um array Numpy com números inteiros de 20 a 50
arraynumber =  np.arange(20,51)

#2.7 criar uma matriz identidade 5x5
arrayiden = np.eye(5)

#2.8 criar um array 1D de 15 elementos que contenha os números de 1 a 15, mas substitua todos os múltiplos de 3 por -1
array1D = np.arange(1,16)
array1D[array1D %3==0] = -1



