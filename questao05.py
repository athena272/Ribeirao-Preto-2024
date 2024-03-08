def inverter_string(texto):
    inverso = ""
    for i in range(len(texto)-1, -1, -1):
        inverso += texto[i]
    return inverso

# Exemplo de uso
texto = input("Digite uma string para ser invertida: ")
print(inverter_string(texto)) # Saída: "odnuM alO"