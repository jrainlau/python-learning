L = range(1, 101)

print L[:10]
print L[2::3]
print L[4:50:5]

L = range(1, 101)
print L[-10:]
print L[-46::5]

def firstCharUpper(s):
    return s[:1].upper() + s[1:]

print firstCharUpper('hello')