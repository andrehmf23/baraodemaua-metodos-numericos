from calculate import Function

function = Function()

limit = int(input("Limite de casas: "))

function.__limit(limit)
function.__function(input("Defina sua função: "))
print("Defina seu intervalo [a,b]: ")
a = round(float(input("a: ")), limit)
b = round(float(input("b: ")), limit)
erro = float(input("Defina sua taxa de erro: "))


print("a, Xn, b, f(a), f(Xn)")
while True:
    # calcular Xn
    Xn = (a + b) / 2

    fa = function.calculate(a)
    fXn = function.calculate(Xn)

    print(a, Xn, b, fa, fXn)

    if abs(fXn) < erro:
        print("Valor prox da raiz: ", b)
        break

    if (fXn < 0 and fa < 0) or (fXn > 0 and fa > 0):
        a = Xn
    else:
        b = Xn
