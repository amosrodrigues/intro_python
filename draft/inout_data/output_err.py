import sys

err = "Arquivo não encontrado"
print(f"Erro aconteceu: {err}", file=sys.stderr)

x = 5
y = 3

print(f"{x} / {y} = {x / y:.2f}")

print(f"{x:.^3}")
