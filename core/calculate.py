from sympy import symbols, ln, sympify, lambdify, diff
import numpy as np


class Function:
    def __init__(self):
        self.__limit = None
        self.__lambdify: lambdify = None
        self.__symbols: symbols = None
        self.__function: sympify = None

    def calculate(self, *args):
        """
          Calcula o valor de uma função.

          Returns:
              O valor da função, ou None em caso de erro.
        """
        if self.__symbols and self.__function:
            self.lambdify()
        else:
            raise TypeError("Valores de symbols ou function indefinido!")

        if isinstance(args, dict):
            return round(self.__lambdify(**args), self.__limit)  # Expande o dicionário como argumentos nomeados
        elif isinstance(args, list) or isinstance(args, tuple):
            return round(self.__lambdify(*args), self.__limit)  # Expande a lista/tupla como argumentos posicionais
        else:
            raise TypeError("Valores devem ser um dicionário, lista ou tupla.")

    def function(self, expressao_str: str):
        """
          Defini a função que será calculada
          Args:
              expressao_str: A expressão da função como string (ex: "xln(x)").
        """

        self.__function = sympify(expressao_str)

    def lambdify(self):
        """
          Cria o processador da função
        """

        try:
            self.__lambdify = lambdify(self.__symbols, self.__function, modules=[{'ln': np.log}, 'numpy'])
        except Exception as e:
            print(f"Erro ao avaliar a função: {e}")
            self.__lambdify = None

    def symbols(self, symbols_str):
        """
          Defini os símbolos que representão as variáveis
          Args:
              symbols_str: As variáveis da expressão da função como string (ex: "x1 a b x2").
        """

        self.__symbols = symbols(symbols_str)

    def limit(self, limit: int):
        self.__limit = limit
