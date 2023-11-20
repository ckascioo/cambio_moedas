import json
from currency_converter import ECB_URL, SINGLE_DAY_ECB_URL
from currency_converter import CurrencyConverter
from datetime import datetime

c = CurrencyConverter(ECB_URL) # Historico completo
c = CurrencyConverter(SINGLE_DAY_ECB_URL) # Taxas recentes

moedas = c.currencies

def intro():
    print('Bem-vindo ao Conversor Universal de Moedas:\n-------------------------------------------')
    valor = float(input('Digite um valor: ').replace(',', '.'))
    return valor ######

def moeda_inicial():
    inicial = input('Escolha uma moeda inicial\n1 - USD\n2 - BRL\n3 - OUTRA\nDigite uma das opções: ')
    if int(inicial) == 1:
        inicial = 'USD'
    elif int(inicial) == 2:
        inicial = 'BRL'
    elif int(inicial) == 3:
        inicial = input('Digite a moeda (3 digitos): ').upper()
    else:
        print('Opção Inválida!')
        return moeda_inicial() 
    return inicial

def moeda_cambio():
    cambio = input('Escolha uma moeda para conversão\n1 - USD\n2 - BRL\n3 - OUTRA\nDigite uma das opções: ')
    if int(cambio) == 1:
        cambio = 'USD'
    elif int(cambio) == 2:
        cambio = 'BRL'
    elif int(cambio) == 3:
        cambio = input('Digite a moeda (3 digitos): ').upper()
    else:
        print('Opção Inválida!')
        return moeda_cambio() 
    return cambio

while True:
    try:
        valor = intro()
        inicial = moeda_inicial()
        cambio = moeda_cambio()
    except ValueError:
        print('Digite um valor valido!')
    else:
        # inicial, cambio = moedas
        # de = inicial
        # para = cambio
        try:            
            data_conversao = datetime.now().strftime('%d/%m/%Y')
            conversao = c.convert(valor, inicial, cambio)
            print(f'Data da cotação: {data_conversao}')
            print(f'{valor:,.2f} {inicial} = {conversao:,.2f} {cambio}')
        except ValueError:
            print('Estamos atualizando o sistema, tente novamente mais tarde!')