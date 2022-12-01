A = [0]
V = [1, 2, 3, 4]
Amin = []

D = [
      [0, 9, 75, 0, 0],
      [9, 0, 95, 19, 42],
      [75, 95, 0, 51, 66],
      [0, 19, 51, 0, 31],
      [0, 42, 66, 31, 0]
    ]

while len(V) != 0:
  minimo = 99999
  
  for j in A:
    for k in V:
      if D[j][k] > 0 and D[j][k] < minimo:
        minimo = D[j][k]
        aresta = [j, k]

  Amin.append(aresta)
  k = aresta[1]
  A.append(k)
  V.remove(k)

print(Amin)