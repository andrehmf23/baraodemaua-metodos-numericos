from calculate import Function

function = Function()

limit = int(input("Limite de casas: "))

function.__limit(limit)

funct = input("Defina sua função: ")
functderivate = input("Defina sua função derivada: ")
print("Defina seu intervalo [a,b]: ")
a = round(float(input("a: ")), limit)
b = round(float(input("b: ")), limit)
erro = float(input("Defina sua taxa de erro: "))
Xn = a

print("i, Xn, f(Xn), erro")
i = 0
c = None

function.__function(funct)
fa = function.calculate(a)
fb = function.calculate(b)
fXn = None

function.__function(functderivate)
dfa = function.calculate(a)
dfb = function.calculate(b)

if fa * dfa > 0:
    c = a
    Xn = b
elif fb * dfb > 0:
    c = b
    Xn = a

while True:
    # calcular Xn
    # Xn = (a + b) / 2

    function.__function(funct)
    fXn = function.calculate(Xn)
    fc = function.calculate(c)
    MfXn = abs(fXn)

    print(i, Xn, fXn, MfXn, c, fc)

    if MfXn < erro:
        print("Valor prox da raiz: ", fXn)
        break

    Xn = (Xn - (fXn * (Xn - c)) / (fXn - fc))

    fXn = function.calculate(Xn)

    i = i + 1
