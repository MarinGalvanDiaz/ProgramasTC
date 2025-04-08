import random

def generar_secuencia(k):
    with open("resultado.txt", "w") as f:
        f.write(f"Σ^{k} = (\n")

        if k == 0:
            f.write("None\n")
        elif k == 1:
            f.write("None\n0\n1\n")
        else:
            f.write("None\n0\n1\n")
            for l in range(2, k+1):
                f.write(bin(0)[2:].zfill(l) + "\n")
                for i in range(1, 2 ** l):
                    f.write(bin(i)[2:].zfill(l) + "\n")
        f.write(")")


def mostrar_menu():
    print("\n--- Menú de Generación de Secuencias Binarias ---")
    print("1. Modo automático (número aleatorio 0-29)")
    print("2. Modo manual (ingresar número)")
    print("3. Salir")
    return input("Seleccione una opción: ")


def main():
    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            k = random.randint(0, 29)
            print(f"\nSe ha seleccionado automáticamente k = {k}")
            generar_secuencia(k)
            print("Archivo 'resultado.txt' generado con éxito!")

        elif opcion == "2":
            try:
                k = int(input("\nIngrese un número entre 0 y 29: "))
                if 0 <= k <= 29:
                    generar_secuencia(k)
                    print("Archivo 'resultado.txt' generado con éxito!")
                else:
                    print("Error: El número debe estar entre 0 y 29")
            except ValueError:
                print("Error: Por favor ingrese un número válido")

        elif opcion == "3":
            print("Saliendo del programa...")
            exit(0)

        else:
            print("Opción no válida. Por favor seleccione 1, 2 o 3")


if __name__ == "__main__":
    main()