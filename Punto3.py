def primo(numero):
  if numero <= 1:
    return False
  s = True        #empezamos asumiendo que el numero SI es primo
  limite = numero**0.5             #usamos de limite la la raiz, para que sea mas eficiente
  for i in range(2, int(limite+1)):  #es "limite+1" para que incluya el limite
    s = s and (numero % i != 0)
  return s


def filtrar_primos(lista):
    primos = []
    for numero in lista:
        if primo(numero):
            primos.append(numero)
    return primos


p = [2,3,25,27]
b =filtrar_primos(p)
print(b)
