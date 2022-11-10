ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

DICIONARIO = {}

for i in range(10):
    DICIONARIO[i] = str(i)

for i in range(0, len(ABC)):
    DICIONARIO[i + 10] = ABC[i]

#------------------------------------------------------------------------------------------------

def separador():
    print("\n---------------------------------------------\n")


def converter(n,b):
    valor = []
    
    while n >= b:
        resultado = n//b
        resto = n%b
        n = resultado
        valor.append(DICIONARIO[resto])
        
    valor.append(DICIONARIO[n] if n > 0 else '')
    
    return ''.join(valor)[::-1]


def entrada():
    while 1:
        num = input('Digite um número inteiro em base decimal: ')
        if num.isdigit(): break
        else: print('\nValor inválido!\n')
    return num


def saida():
    while 1:
        continua = input("Deseja fazer outra operação? (S/N) ")
        if (continua == "N" or continua == "S" or continua == "n" or continua == "s"): break
        else: print("Por favor, somente 'S' ou 'N' como resposta.")
    return continua

#------------------------------------------------------------------------------------------------

while 1:
    num = entrada()

    for i in range(2, len(DICIONARIO) + 1):
        print('Base', str(i) + ':', converter(int(num), i))

    separador()
    
    continua = saida()

    if (continua in ['n', 'N']): break
    else: separador()
