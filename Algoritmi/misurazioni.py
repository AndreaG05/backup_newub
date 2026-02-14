# Esercizio 1
lower = 20
upper = 70

def check_consecutive_alert(values, lower, upper, N):
    count = 0
    start_index = None
    
    for i, val in enumerate(values):
        if val < lower or val > upper:
            if count == 0:
                start_index = i
            count += 1        
            if count == N:
                return (True, start_index)
        else:
            count = 0
            start_index = None
    return (False, None)

# STEP 1
values = []

num_misurazioni = int(input("Quante misurazioni vuoi inserire? "))

for i in range(num_misurazioni):
    val = int(input(f"Inserisci misurazione {i+1}: "))
    
    values.append(val)
    allarme, indice = check_consecutive_alert(values, lower, upper, 3)
    
    if allarme:
        print(f"[!] ALERT attivato all'indice {indice}")
        break

# STEP 2 - Gestione pazienti
patients = {}

def add_measurement(patients, name, value):
    if name not in patients:
        patients[name] = []
        
    patients[name].append(value)

num_pazienti = int(input("Quanti pazienti? "))

for i in range(num_pazienti):
    nome = input(f"\nPaziente {i+1} - Nome: ")
    num_mis_paziente = int(input(f"Quante misurazioni per {nome}? "))
    
    for j in range(num_mis_paziente):
        mis = int(input(f"  Misurazione {j+1}: "))
        add_measurement(patients, nome, mis)
        
    # Controlla allarme dopo tutte le misurazioni
    allarme, indice = check_consecutive_alert(patients[nome], lower, upper, 3)
    
    if allarme:
        print(f"[!] ALERT per {nome} (indice: {indice})!")

        
# STEP 3 - Report
def report_alerts(patients, lower, upper, N):
    print("ALLARMI ATTIVI:")
    allarmi_trovati = False
    
    for nome, misurazioni in patients.items():
        allarme, start_index = check_consecutive_alert(misurazioni, lower, upper, N)
        if allarme:
            allarmi_trovati = True
            print(f"  {nome} -> {N} misure consecutive fuori soglia (indice: {start_index})")
    
    if not allarmi_trovati:
        print("  Nessun allarme attivo\n")

        
report_alerts(patients, lower, upper, 3)
print("Dizionario pazienti:", patients)
