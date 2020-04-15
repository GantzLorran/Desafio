'''Dado um array de números inteiros, retorne os índices dos dois números de forma que eles se
somem a um alvo específico.
Você pode assumir que cada entrada teria exatamente uma solução, e você não pode usar o
mesmo elemento duas vezes.
Exemplo:
Dado nums = [2, 7, 11, 15], alvo = 9,
Como nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''
listaNumber = [1,2,3,4,5,6,7,8,9]
lista = []
soma = 0

num = int(input('Digite um número: '))
for index, number in enumerate(listaNumber):
    for indice, numbers in enumerate(listaNumber):
        if index != indice:
            soma = number + numbers
            if soma == num:
                lista.append(index)
                lista.append(indice)
print(f'Os números {lista[2]} e {lista[1]} somam o número {num}')