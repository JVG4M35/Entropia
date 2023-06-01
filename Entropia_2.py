import math

def calculate_entropy(values, frequencies):
    entropy = 0

    for frequency in frequencies:
        entropy -= frequency * math.log2(frequency)

    return entropy

# Valores e suas frequências relativas
values = [1, 2, 3, 4, 5]
frequencies = [0.1, 0.2, 0.3, 0.4, 0.5]

# Cálculo da entropia
entropy = calculate_entropy(values, frequencies)

# Maior e menor valor
min_value = min(values)
max_value = max(values)

# Exibição dos resultados
print("Valores: ", values)
print("Frequências: ", frequencies)
print("Menor valor: ", min_value)
print("Maior valor: ", max_value)
print("Entropia: ", entropy)

