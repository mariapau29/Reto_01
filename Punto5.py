def anagrama(lista):
  resultado = []
  for i in range(len(lista)):    #i es la primera palabra a comparar
    for j in range(i+1,len(lista)):   #j es la segunda palabra a comparar
      if sorted(lista[i])== sorted(lista[j]):
        if lista[i] not in resultado:
          resultado.append(lista[i])
        if lista[j] not in resultado:
          resultado.append(lista[j])
  return resultado

p = ["amor", "roma", "perro"]
b = anagrama(p)
print(b)
