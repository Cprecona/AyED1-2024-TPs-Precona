oblongo = lambda x: any(x == k * (k + 1) for k in range(1, int(x**0.5) + 1))


print(oblongo(6))
