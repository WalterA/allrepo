#stampare l'elenco dei parametri passati sulla riga di comando
#Esempio :python prova.py uno due tre
# devo stampare uno , due , tre
import sys
if len(sys.argv) <3:
    print("Expected: " + sys.argv[0]+ " Numero numero")
    sys.exit(-1)
    
num1 = float(sys.argv[1])
nums2= float ( sys.argv[2])

print(num1+nums2)  # stampa i due numeri passati sulla riga

for s in sys.argv:
    print(s)

