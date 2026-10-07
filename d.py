import sympy as sp

N = 1

while True:
    nums = [N, N+1, N+2, N+3]

    # N में कोई digit repeat नहीं होना चाहिए
    if len(str(N)) != len(set(str(N))):
        N += 1
        continue

    sums = []

    for x in nums:
        factors = sp.factorint(x)
        prime_sum = sum(factors.keys())
        sums.append(prime_sum)

    if sums == [100, 101, 102, 103]:
        print("FOUND!")
        print("N =", N)
        print("Numbers =", nums)
        print("Prime-factor sums =", sums)
        break

    N += 1