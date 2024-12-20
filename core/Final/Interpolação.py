import numpy as np
import sympy

def lagrange_interpolation_symbolic(x_values, y_values):
    """
    Calcula a função interpoladora de Lagrange usando sympy para representação simbólica.
    """
    x = sympy.Symbol('x')
    n = len(x_values)
    polynomial = 0

    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if i != j:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        polynomial += term
    return polynomial


def lagrange_interpolation(x_values, y_values):
    """
    Calcula a função interpoladora de Lagrange (versão numérica).
    """
    n = len(x_values)
    if len(x_values) != len(y_values):
        print("Erro: O número de valores x e y deve ser o mesmo.")
        return None
    if n == 0:
        print("Erro: Nenhum ponto fornecido.")
        return None

    def lagrange_basis(i, x):
        basis = 1.0
        for j in range(n):
            if i != j:
                basis *= (x - x_values[j]) / (x_values[i] - x_values[j])
        return basis

    def interpolating_function(x):
        result = 0.0
        for i in range(n):
            result += y_values[i] * lagrange_basis(i, x)
        return result

    return interpolating_function


# Solicita a entrada do usuário
try:
    num_points = int(input("Digite o número de pontos: "))
    x_values = []
    y_values = []
    for i in range(num_points):
        x = float(input(f"Digite o valor de x{i+1}: "))
        y = float(input(f"Digite o valor de y{i+1}: "))
        x_values.append(x)
        y_values.append(y)

    # Verifica se os pontos x são distintos
    if len(set(x_values)) != num_points:
        print("Erro: Os valores de x devem ser distintos.")
    else:
        # Calcula a função interpoladora (versão simbólica)
        interpolating_func_symbolic = lagrange_interpolation_symbolic(x_values, y_values)

        # Calcula a função interpoladora (versão numérica)
        interpolating_func_numeric = lagrange_interpolation(x_values, y_values)

        if interpolating_func_numeric:
            # Solicita o ponto para avaliação
            x_eval = float(input("Digite o valor de x para avaliação: "))

            # Avaliação numérica
            y_eval_numeric = interpolating_func_numeric(x_eval)
            print(f"O valor interpolado (numérico) para x = {x_eval} é y = {y_eval_numeric}")

            # Avaliação simbólica (opcional, para comparação)
            x_eval_sym = sympy.Symbol('x_eval')
            numeric_func_sym = sympy.lambdify(sympy.Symbol('x'), interpolating_func_symbolic, modules=['numpy'])
            y_eval_symbolic = numeric_func_sym(x_eval)
            print(f"O valor interpolado (simbólico) para x = {x_eval} é y = {y_eval_symbolic}")


            # Mostra a função interpoladora em forma simbólica
            print("\nFunção Interpoladora (forma simbólica):")
            print(interpolating_func_symbolic)

            # Mostra a função interpoladora (forma numérica, para fins de demonstração)
            print("\nFunção Interpoladora (forma numérica):")
            print(interpolating_func_numeric)


except ValueError:
    print("Erro: Entrada inválida. Certifique-se de inserir números.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")