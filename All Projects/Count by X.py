def count_by(x, n):
    result = []
    for i in range(1, n + 1):
        result.append(x * i)
    return result

x = int(input("Starter point: "))
n = int(input("End point: "))
multiples = count_by(x, n)

print(f"The first {x} multiples of {n} are: {multiples}")

