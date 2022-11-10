import requests
import json

class ListaDeRepositorios():
    def __init__(self, usuario):
        self._usuario = usuario
	
    def requisicao_api(self):
        resposta = requests.get(f'https://api.github.com/users/{self._usuario}/repos')
        if resposta.status_code == 200:
            return resposta.json()
        else:
            return resposta.status_code
    def imprime_repositorios(self):
        dados_api = self.requisicao_api()
        if type(dados_api) is not int:
            print(f'Repositórios públicos do usuário {self._usuario}:\n')
            for i in range(len(dados_api)):
                print(dados_api[i]['name'])
        else:
            print(dados_api)
            

usuario = input("Digite um nome de usuário do GitHub: ")
print('\n')

repositorios = ListaDeRepositorios(usuario)
repositorios.imprime_repositorios()

input()
