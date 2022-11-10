class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name + " tem " + str(self.age) + " ano(s) de idade."

    def miar(self):
        print(self.name + ": MIAU!!!")

kate = Cat("Kate", 3)
channel = Cat("Channel", 2)

print(kate)
print(channel)

print()

kate.miar()
channel.miar()
channel.miar()
kate.miar()
input()