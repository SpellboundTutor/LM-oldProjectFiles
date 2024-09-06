def RecursiveProduct(N):
    if N == 1:
        print(f"{N}", end="")
        return N
    else:
        print(f"{N} * (",end="")
        prod = N * RecursiveProduct(N-1)
        print(")", end="")
        return prod
    