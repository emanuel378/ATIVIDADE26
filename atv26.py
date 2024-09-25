# Crie um programa que receba as notas de 5 alunos e as armazene em uma lista. O programa deve exibir a maior nota, a menor nota e a média das notas.

# Exemplo de entrada:
# Nota do aluno 1: 8
# Nota do aluno 2: 6
# Nota do aluno 3: 9
# Nota do aluno 4: 7
# Nota do aluno 5: 5

# Exemplo de saída:
# Maior nota: 9
# Menor nota: 5
# Média das notas: 7.0

soma = 0
contador = 0
lista = []
for c in range(5):
    num=int(input("Digite um numero"))
    lista.append(num)
    lista.sort(key=int,reverse=True)
    print(lista)
    soma+=num
    contador+=1
    if contador>0:
        media = soma/contador

    
    
     

print(f"a maior nota e: {lista[0]}")
print(f"A menor nota e : {lista[4]}")
print('Media das notas : {}'.format(media))
    
