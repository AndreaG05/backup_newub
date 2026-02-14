# ESERCIZIO UPDATED MISURAZIONI

lista_valori = []
N = int(input("Quante misurazioni vuoi inserire? "))

for i in range(N):
    mis = int(input("Inserisci la misurazione: "))
    lista_valori.append(mis)

def get_baseline(lista_valori):
    if len(lista_valori) < 6:
        return None
    
    last5num = lista_valori[-6:-1]
    media = sum(last5num) / 5
    
    return media


def check_anomaly(valore_attuale, soglia):
    return valore_attuale > soglia


def verify_consecutive_alert(lista_valori, N):
    if len(lista_valori) < N + 5:
        return (False, None)
    
    count_anomale = 0
    start_index = None

    # Parte da indice 5 perché servono 5 valori prima per fare la media.
    for i in range(5, len(lista_valori)):
        valore_corrente = lista_valori[i]
        
        precedenti_5 = lista_valori[i-5:i]
        media = sum(precedenti_5) / 5
        soglia = media * 1.20
        
        if check_anomaly(valore_corrente, soglia):
            if count_anomale == 0:
                start_index = i
            count_anomale += 1
            
            if count_anomale == N:
                return (True, start_index)
        else:
            count_anomale = 0
            start_index = None
    
    return (False, None)


print("Media:", get_baseline(lista_valori))
print("Lista valori:", lista_valori)

allarme, indice = verify_consecutive_alert(lista_valori, 3)

if allarme:
    print(f"ALLARME! Indice inizio: {indice}")
else:
    print("Nessun allarme")
