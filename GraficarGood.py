"""k = 30  # Número de caracteres del alfabeto binario

with open("resultadogood.txt", "w") as f:
    for l in range(1, k):  # Empezar desde 1 para evitar (0)
        for i in range(2 ** l):
            bin_str = bin(i)[2:].zfill(l)  # Convertir a binario con ceros a la izquierda
            count_ones = bin_str.count('1')  # Contar los 1s
            f.write(f"{l} {count_ones}\n")  # Formato: "longitud cantidad_de_unos"""
k = 30  # Máxima longitud de cadena binaria

with open("resultadogood.txt", "w") as f:
    f.write(f"0\n")
    for l in range(1, k):
        for i in range(2 ** l):
            count_ones = bin(i).count('1')  # Contar los 1s en el número binario
            f.write(f"{count_ones}\n")  # Guardar solo `y`