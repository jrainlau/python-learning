def average(*args):
    sum = 0.0
    if len(args) == 0:
        return sum
    else:
        for item in args:
            sum += item
        return sum/len(args)

print average(1, 2, 3)
