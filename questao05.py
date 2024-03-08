def inverter_string(texto):
    inverso = ""
    for i in range(len(texto)-1, -1, -1):
        inverso += texto[i]
    return inverso

# Exemplo de uso
texto = input("Digite um número para verificar: ")
print(inverter_string(texto)) # Saída: "odnuM alO"