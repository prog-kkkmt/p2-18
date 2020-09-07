

def Fib(N, Sch):
    Sch.append(1);
    if N == 0:
        return 0
    if N == 1:
        return 1
    return Fib(N - 1, Sch) + Fib(N - 2, Sch)
Nn = int(input("Сколько чисел вы хотите вывести: "))
while Nn > 0:
    sch = []
    n = int(input("N = "))
    print("\n", Fib(n, sch), len(sch))
    Nn -= 1
