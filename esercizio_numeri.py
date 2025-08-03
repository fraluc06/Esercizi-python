x = input("Inserisci un numero: ")
x = int(x)
y = input("Inserisci un altro numero: ")
y = int(y)
z = input("Inserisci un terzo numero: ")
z = int(z)
prova = (x*100 + y*10)/ z
print(f"Il primo numero è intero? {x.is_integer()}.\nIl tipo del secondo è:{type(y)}\nIl risultato dell'operazione è: {abs(z)+pow(z,3)}")