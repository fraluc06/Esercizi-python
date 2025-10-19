#Esercizio 1
numeri = [x for x in range(1,11)]
x = 11
numeri.insert(0, 0)
numeri.append(x)
numeri.pop(numeri.index(5))
n = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
somma = sum(n)
print(somma)
print(max(n))
print(min(n))
print(n.count(1))
pari = [num for num in n if num %2 ==0]
print(pari)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
diag_matrix = [matrix[i][i] for i in range(len(matrix))]
print(diag_matrix)

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c':4, 'd': 5}
merged_dict = {}
for k in ['a', 'b', 'c', 'd']:
    merged_dict[k] = dict1.get(k, 0) + dict2.get(k, 0)
print(merged_dict)
# Il tuo codice qui
# Risultato atteso: {'a': 1, 'b': 5, 'c': 7, 'd': 5}