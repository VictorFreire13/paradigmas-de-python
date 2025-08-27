nome1 = float(input("digite a primeira nota:"))
nome2 = float(input("digite a segunda nota:"))
nome3 = float(input("digite a terceira nota:"))
nome4 = float(input("digite a quarta nota:"))
media = (nome1 + nome2 + nome3 + nome4) / 4
print("A média é:", media)
if media >=7:
    print("Aprovado")
else:
    print("Reprovado")