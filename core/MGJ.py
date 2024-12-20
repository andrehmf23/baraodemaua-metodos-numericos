from calculate import Function

"""
(32-5*x2-x3)/20
(-20-2*x3+2*x1)/10
(14-x1-4*x2)/10

(1+x2)/2
(3-x1)/2
"""

function = Function()

totaleq = int(input("Digite o total de equações: "))
esperado = float(input("Defina sua taxa de erro: "))

symbols = str(input("Defina suas variáveis: "))
function.symbols(symbols)
limit = int(input("Limite de casas: "))
function.limit(limit)

functs: list = []
xs: list = []
xshadow: list = []


i = 0
while i < totaleq:
    functs += [str(input(f"Defina sua função{i}: "))]
    xs += [round(float(input(f"X{i}: ")), limit)]
    i += 1

print("| i ", end='')
i = 0
while i < totaleq:
    print(f"| X{i + 1} | Erro {i + 1} |", end='')
    i += 1
print()

while True:

    xshadow = xs.copy()
    verify: bool = True
    i = 0
    while i < totaleq:
        function.function(functs[i])
        xs[i] = function.calculate(*xshadow)

        subtract = abs(round(xs[i] - xshadow[i], limit))
        erro = subtract < esperado
        verify = erro and verify
        print()
        print(f"|{xs[i]} - {xshadow[i]}| < {esperado}")
        print(f"{subtract} < {esperado} = {erro}")
        print()
        i += 1

    if verify:
        print(f"O resultado é {xs}")
        break

    print(i, xs, xshadow, verify)

    i = i + 1
