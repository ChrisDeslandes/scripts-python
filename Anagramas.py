def anagramas(palavra):
    if len(palavra) <=1:
        return palavra
    else:
        tmp = []
        for aux in anagramas(palavra[1:]):
            for i in range(len(palavra)):
                p = aux[:i] + palavra[0:1] + aux[i:]
                if not p in tmp:
                    tmp.append(p)
        return tmp

def fat(n):
    return 1 if n < 2 else fat(n-1) * n

def nAnagramas(palavra):
    letrasDistintas = list(dict.fromkeys(';;'.join(palavra).split(';;')))
    letrasRepetidas = []
    for i in letrasDistintas:
        cont = 0
        for j in palavra:
            if i == j:
                cont += 1
        letrasRepetidas.append(cont)
    letrasRepetidas = list(filter(lambda n: n != 1, letrasRepetidas))
    total = fat(len(palavra))
    for n in letrasRepetidas:
        total /= fat(n)
    return int(total)


while True:
    palavra = input('Digite uma palavra para saber o número de anagramas possíveis: ').strip().upper()
    
    totalAnagramas = nAnagramas(palavra)
    totalAnagramasStr = f'{totalAnagramas:,.0f}'.replace(',','.')
    
    print('\n\nExistem ' + totalAnagramasStr + ' anagramas distintos para a palavra \'' + palavra + '\'.')

    if totalAnagramas <= 12000:
        print('São eles:\n')
        todosAnagramas = anagramas(palavra)
        todosAnagramas.sort()
        if totalAnagramas <= 1000:
            for i, anagrama in enumerate(todosAnagramas, start=1):
                print(f'{i:,.0f}'.replace(',','.') + ' - ' + anagrama)
        else:
            print(' - '.join(todosAnagramas))

    resp = input('\n\nDeseja fazer outro cálculo? (s para sim) ').strip().lower()
    if not resp in ['s', 'sim']:
        break
    print('\n----------------------------------------------------------------------------------------\n')
