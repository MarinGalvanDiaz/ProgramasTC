k = 30  # Número de caracteres del alfabeto binario
with open("resultado.txt", "w") as f:
    f.write(f"Σ^{k - 1} = (\n")  # Escribir la cabecera con salto de línea

    # Escribir los primeros valores sin usar una lista
    f.write("None\n0\n1\n")  # Cada uno en una línea

    for l in range(2, k):
        f.write(bin(0)[2:].zfill(l) + "\n")  # Escribir el primer valor de cada longitud
        for i in range(1, 2 ** l):
            f.write(bin(i)[2:].zfill(l) + "\n")  # Escribir cada número binario en una línea

    f.write(")")  # Cerrar con paréntesis final