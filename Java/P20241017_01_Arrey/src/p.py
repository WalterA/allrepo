"""dichiarare una lista inserire nella lista  inserire nella lista 
1000 valori casuali compresi tra 0 e 100 contare quanti elementi sono minori di 50"""
import random
lista = [0]*1000
conta=0
for i in lista:
    lista[i]= random.uniform(0,100)
    if lista[i]<50:
        conta+=1
print(conta)