def mayor_suma_numeros(lista):
  if len(lista)<2:
    return None
  variable = lista[0] + lista[1]
  for i in range(1, len(lista)-1):
      suma = lista[i] + lista[i+1]
      if suma > variable:
         variable = suma
  return variable

p = [3, 8, -2, 5, 10, -1]
b = mayor_suma_numeros(p)
print(b)
