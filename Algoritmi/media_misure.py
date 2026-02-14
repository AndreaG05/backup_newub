# Scrivi una func che:
# - riceve una lista di n
# - restituisce la media

def calcola_media(valori):
    if len(valori) == 0:
        return 0

    media = sum(valori) / len(valori)
    return media

numeri = []
q = int(input("Quanti numeri vuoi inserire? "))

for i in range(q):
    n = float(input(f"Inserisci numero {i+1}: ")) 
    numeri.append(n) 

if len(numeri) > 0:
    risultato = calcola_media(numeri)
    print(f"La media è: {risultato}")
else:
    print("Nessun numero inserito.")

