ano = int(input('Informe um ano qualquer (ex: 2024): '))

if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print(f'O ano de {ano} é bissexto.')
else:
    print(f'O ano de {ano} não é bissexto.')