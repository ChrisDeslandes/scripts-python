import requests
import hashlib
import os

#dicionario = "AÁBCDEÉFGHIÍJKLMNOÓPQRSTUVWXYZaáâãbcçdeéêfghiíjklmnoóôõpqrstuúvwxyz0123456789 .-_*@&"

alfabeto = 'abcdefghijklmnopqrstuvwxyz'

url = 'http://divertidodeaprender.hospedagemdesites.ws/?password='

negativa = "{\"password\":\"Errou\",\"passwordcripto\":\"Errou\"}"

senha = ''
senhacorreta = ''

# A senha correta para este site é 'vv'. A senha criptografada eu não descobri!

while True:
    for i in alfabeto:
        for j in alfabeto:
            senha = i + j
            print("Tentando senha:", senha)
            r = requests.get(url + senha)
            if r.text != negativa:
                senhacorreta = senha
                print('\n\nRequisição: ', url + senha)
                print('Resposta: ', r.text)
                break
        if senhacorreta != '': break
    if senhacorreta != '': break
    
    for i in alfabeto:
        for j in alfabeto:
            for k in alfabeto:
                senha = i + j + k
                print("Tentando senha:", senha)
                r = requests.get(url + senha)
                if r.text != negativa:
                    senhacorreta = senha
                    print('\n\nRequisição: ', url + senha)
                    print('Resposta: ', r.text)
                    break
            if senhacorreta != '': break
        if senhacorreta != '': break
    if senhacorreta != '': break
    
    for a1 in alfabeto:
        for a2 in alfabeto:
            for a3 in alfabeto:
                for a4 in alfabeto:
                    senha = a1 + a2 + a3 + a4
                    print("Tentando senha:", senha)
                    r = requests.get(url + senha)
                    if r.text != negativa:
                        senhacorreta = senha
                        print('\n\nRequisição: ', url + senha)
                        print('Resposta: ', r.text)
                        break
            if senhacorreta != '': break
        if senhacorreta != '': break
    if senhacorreta != '': break
    
print("\n\nSenha Correta:", senha)

print("\nSenha criptografada com MD5:", str(hashlib.md5(senha.encode())))

print("\nPressione qualquer tecla para fechar...")
os.system("pause >nul")
