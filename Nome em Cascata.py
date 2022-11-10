print()

c = input("Digite o nome / frase: ")
cReversa = c[::-1]

if (c == cReversa):
	print("\nÉ palíndromo!")

print()

separacao = 1

for i in range(len(c)):
	print(c[:i + 1] + "." * (2 * (len(c) - len(c[0:i+1])) + separacao) + cReversa[len(c) - 1 - i:])

for i in range(1, len(c)):
	print(c[:len(c) - i] + "." * (2 * (len(c) - len(c[0:len(c) - i])) + separacao) + cReversa[i:])

input()
