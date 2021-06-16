def Fib(n, S):
    S.append(1);
    if n == 0:
        return 0
    if n == 1: 
        return 1
    return Fib(n - 1, S) + Fib(n - 2, S)
S = []
n = int(input("N = "))
print(Fib(n, S), len(S))
