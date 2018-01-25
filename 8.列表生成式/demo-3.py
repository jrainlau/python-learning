L = ['Hello', 'World', 18, 'Apple', None]

L1 = [i.lower() for i in L if isinstance(i, str)]

print(L1)

xx = ['xxx-{}-yuyy'.format(str(i)) for i in range(1, 100, 5)]

print(xx)