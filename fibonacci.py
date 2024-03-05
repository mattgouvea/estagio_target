def fib(n):
    sequencia = [0, 1]
    x = 0
    while x <= n:
        if x == n:
            print("Pertence a sequencia")
            return
        else:
            x = sequencia[0] + sequencia[1]
            sequencia[0] = sequencia[1]
            sequencia[1] = x
    
    print("Não pertence a sequencia")
    return

fib(0)