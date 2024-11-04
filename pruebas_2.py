# Supongamos que tienes un arreglo 2D
arreglo_2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Voltear verticalmente el arreglo 2D
arreglo_volteado = arreglo_2d[::-1]

# Imprimir el resultado
for fila in arreglo_volteado:
    print(fila)
    
a = [fila for fila in arreglo_volteado]
print(a)
