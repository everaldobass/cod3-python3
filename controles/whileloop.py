# Loops
nota = 0
total = 0
qtde = 0

while nota != -1:
    nota = float(input("Informe o número ou -1 para sair: "))

    if nota != -1:
        qtde += 1
        total += nota

print(f'A média da turma é {total / qtde}')