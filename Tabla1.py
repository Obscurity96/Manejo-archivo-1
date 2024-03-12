def generar_tabla(numero):
    if numero < 1 or numero > 10:
        print("Error: El número debe estar entre 1 y 10.")
        return
    
    archivo = f"tabla{numero}.txt"
    
    try:
        with open(archivo, "x") as f:
            for i in range(1, 11):
                resultado = numero * i
                f.write(f"{numero} x {i} = {resultado}\n")
        print(f"Tabla de multiplicar para {numero} generada exitosamente en {archivo}.")
    except FileExistsError:
        print("Error: Tabla ya generada.")

def main():
    try:
        numero = int(input("Ingrese un número entre 1 y 10: "))
        generar_tabla(numero)
    except ValueError:
        print("Error: Ingrese un número válido.")

if __name__ == "__main__":
    main()
