def palindrome(palabra):
  n = len(palabra)
  for i in range(n//2):
    if palabra[i] != palabra[n - 1 - i]:
      return False
  return True

a = "amor"
b = palindrome(a)
print(b)
