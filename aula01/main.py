
#contador de notas e media com while para a aula de python
qtde = int(input("digita a quantidade de notas: "))
soma = 0
cont = 0
while cont < qtde:
    nota = float(input(f"digite a sua {cont + 1}º nota:"))
    soma += nota
    cont += 1
media = soma / qtde
print('sua media é:', format(media, '.2f'))
if media >= 7:
    print('aprovado')
else:
    print('reprovado')