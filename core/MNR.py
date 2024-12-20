from calculate import Function

function = Function()

limit = int(input("Limite de casas: "))

function.__limit(limit)

funct = input("Defina sua função: ")
functderivate1 = input("Defina sua função derivada: ")
functderivate2 = input("Defina sua função derivada de segundo grau: ")
print("Defina seu intervalo [a,b]: ")
a = round(float(input("a: ")), limit)
b = round(float(input("b: ")), limit)
esperado = float(input("Defina sua taxa de erro: "))
Xn = a

i = 0
c = None
fXn = None

function.__function(funct)
fa = function.calculate(a)
fb = function.calculate(b)

function.__function(functderivate2)
d2fa = function.calculate(a)
d2fb = function.calculate(b)

if fa * d2fa > 0:
    Xn = a
elif fb * d2fb > 0:
    Xn = b

save = None
erro = None

print("i, Xn, f(Xn), f'(Xn), erro")

while True:
    function.__function(funct)
    fXn = function.calculate(Xn)
    function.__function(functderivate1)
    fd1Xn = function.calculate(Xn)

    print(i, Xn, fXn, fd1Xn, erro)
    if save is not None:
        erro = round(save - Xn, limit)
        if abs(erro) < esperado:
            print("Valor prox da raiz: ", Xn)
            break

    save = Xn
    Xn = round(Xn - (fXn / fd1Xn), limit)

    i = i + 1
