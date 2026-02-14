# Slicing

numeri = [0, 1, 2, 3, 4, 5, 6, 7]

# lista[start:end:incremento] -> start è incuso, end è escluso

print(numeri[3:7]) # OUTPUT: [3, 4, 5, 6, 7]

# Con incremento
print(numeri[3:7:2]) # OUTPUT: [3, 5]

# Prendere lista al contrario
print(numeri[7::-1]) # OUTPUT: [7, 6, 5, 4, 3, 2, 1, 0]
print(numeri[-6:-1]) # OUTPUT: [2, 3, 4, 5, 6]
