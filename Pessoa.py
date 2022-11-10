from classes.Pessoa import Pessoa

p1 = Pessoa("Christiano", "086.792.926-05")
p2 = Pessoa("Leslie", "378.515.946-34", 64)
p3 = Pessoa("Daniel", "073.621.586-70")
p4 = Pessoa("Joaquim", "118.101.906-06", 68)

p1.greeting = "Eu sou muito foda!!!"
p3.greeting = "Eu sou policial federal!!!"

listPessoas = [p1, p2, p3, p4]

for p in listPessoas:
    p.mostraDados()

input()
