import timeit

z = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(z)

z2 = timeit.timeit(lambda: "-".join(map(str, range(100))), number=10000)
print(z2)

z3 = timeit.timeit('char in text', setup='text = "sample string"; char = "g"')
print(z3)