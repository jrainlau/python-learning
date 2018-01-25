def power(x, n=2):
  s = 1
  while n > 0:
    n -= 1
    s *= x
  return s

print(power(3))