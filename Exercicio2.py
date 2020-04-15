lista = [7,1,5,3,6,4]
sub = 0

diaCompra = int(input('dia da compra: '))
precoCompra = float(input('Preço da compra: '))
diaVenda = int(input('Dia da venda: '))
precoVenda = float(input('Preço da venda: '))
if diaCompra >= 1 and precoCompra >= 1:
    sub = precoCompra - precoVenda
    print(f'O seu lucro foi de {sub}')
elif diaCompra <= 0:
    print('Nesse caso nenhuma transação deve ser feita, lucro máximo igual a 0')
