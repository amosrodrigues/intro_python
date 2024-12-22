frase = "CS é bom demais, as dicas pythonicas fazem ficar melhor ainda"

vogais = "aeiou"

# lista_vogais = []
# for letra in frase:
#     if letra.lower() in vogais:
#         lista_vogais.append(letra)

# print(lista_vogais)

lista_vogais = [letra for letra in frase if letra.lower() in vogais]

print(lista_vogais)
# Saída: ['o', 'e', 'a', 'i', 'a', 'i', 'a', 'o', 'i', 'a', 'a', 'e', 'i', 'a', 'e', 'o', 'a', 'i', 'a']

# conjunto_vogais = set()
# for letra in frase:
#     if letra.lower() in vogais:
#         conjunto_vogais.add(letra)

# print(conjunto_vogais)

conjunto_vogais = set(letra for letra in frase if letra.lower() in vogais)
print(conjunto_vogais)  # Saída: {'a', 'e', 'o', 'i'}

nomes_1 = ["Felps", "Carlos", "Will", "Bux"]
nomes_2 = ["Flávio", "Carlos", "Roni", ""]

print(all(nomes_1))  # Saída: True
print(all(nomes_2))  # Saída: False

print(any(nomes_1))  # Saída: True
print(any(nomes_2))  # Saída: True

for item in enumerate(nomes_1):
    print(item)
# Saída:
# (0, 'Felps')
# (1, 'Carlos')
# (2, 'Will')
# (3, 'Bux')

for index, item in enumerate(nomes_1, 1):
    print(f"{index}: {item}")
# Saída:
# 0: Felps
# 1: Carlos
# 2: Will
# 3: Bux
