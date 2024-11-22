def isolamento(f, a, b, k, max_iter=1000):
    interv = []
    i = 0
    while a <= b and i < max_iter:
        x = a + k
        if f(a) * f(x) < 0:
            interv.append(a, k)
        i = i + 1
        a = k
    

def bissecao(f, a, b, e=10e-6, max_iter=1000):
    if f(a) * f(b) > 0:
        return
    intervalo = abs(b - a)
    cont = 0
    while intervalo > e and f(x) > e and cont < max_iter:
        x = (a + b) / 2
        fx = f(x)
        if f(a) * fx > 0:
            a = x
        else:
            b = x
        intervalo = intervalo / 2
        cont += 1