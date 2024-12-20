import sympy as sp


def diferencas_divididas_simb(x, y):
    """
    Calcula os coeficientes de diferenças divididas de Newton usando sympy para precisão simbólica.
    """
    n = len(y)
    tabela = [[0] * n for _ in range(n)]
    tabela = sp.Matrix(tabela)
    tabela[:, 0] = y  # A primeira coluna é y

    for j in range(1, n):
        for i in range(n - j):
            tabela[i, j] = (tabela[i + 1, j - 1] - tabela[i, j - 1]) / (x[i + j] - x[i])

    return tabela[0, :]  # Retorna apenas os coeficientes da linha superior


def polinomio_newton_simb(x, y):
    """
    Retorna o polinômio de Newton em forma simbólica.
    """
    # Converte os pontos x e y para valores simbólicos
    x = [sp.Rational(xi) for xi in x]
    y = [sp.Rational(yi) for yi in y]

    coeficientes = diferencas_divididas_simb(x, y)
    x_sym = sp.Symbol('x')  # Variável simbólica para x
    n = len(coeficientes)

    # Inicializa o polinômio como expressão simbólica
    polinomio_simb = coeficientes[0]
    termo = 1  # Inicia o termo que vai sendo multiplicado em cada etapa

    for i in range(1, n):
        termo *= (x_sym - x[i - 1])
        polinomio_simb += coeficientes[i] * termo

    # Expande o polinômio para forma algébrica completa
    polinomio_expandido = sp.expand(polinomio_simb)
    return polinomio_expandido


# Pontos de exemplo
x = [-2, -1, 0, 1, 2]
y = [14, -12, -14, -16, -18]

# Gera o polinômio interpolador expandido
polinomio_expandido = polinomio_newton_simb(x, y)

# Exibe a forma algébrica do polinômio
print("Polinômio interpolador expandido:")
sp.pprint(polinomio_expandido)
