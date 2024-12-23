valors = input("Digite valores numéricos separados por espaço: ")
total = 0
for valor in valors.split(" "):
    if not valor.isdigit():
        print(f"Erro ao somar valores, {valor} é um valor inválido.")
    else:
        total += int(valor)

print(f"A soma total dos valores válidos é: {total}")
