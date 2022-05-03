# If
nota = float(input("Informe a nota do aluno: "))

if nota >= 9:
    print("Duas palavras: para bens! ")
    print("Nota Final: ", nota)
elif nota >= 7:
    print("Aprovado")
    print("Nota Final: ", nota)
elif nota >= 5:
    print("Recuperação")
    print("Nota Final: ", nota)
else:
    print("Reprovado")
    print("Nota Final: ", nota)