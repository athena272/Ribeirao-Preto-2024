def gerar_sequencia_fibonacci(limite):
    """Gera a sequência de Fibonacci até o limite especificado."""
    sequencia = [0, 1]
    while sequencia[-1] < limite:
        sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia

def verificar_fibonacci(numero):
    """Verifica se um número está na sequência de Fibonacci."""
    # Gerar a sequência de Fibonacci até um limite suficientemente grande
    # Neste caso, vamos usar o dobro do número + 1 como limite
    sequencia = gerar_sequencia_fibonacci(numero * 2 + 1)
    if numero in sequencia:
        return f"O número {numero} PERTENCE à sequência de Fibonacci."
    else:
        return f"O número {numero} NÃO PERTENCE à sequência de Fibonacci."

# Exemplo de uso
numero = int(input("Digite um número para verificar: "))
print(verificar_fibonacci(numero))