"""
Método da Bissecção
descrição: O objetivo se trata de aproximar dois pontos de um função até conseguir
o valor aproximado da raiz, considerando uma determinada taxa de erro.

Dados de entrada:
    Intervalo [a,b]
    Taxa de erro desejada 'e'
    Função 'f(x)'

1) Verifique se f(a)*f(b)<0 : Se existe raiz

2) Xn = (a+b)/2 : Novo ponto de aproximação
3) Se f(Xn) tiver mesmo sinal de f(a) -> a = Xn caso contrario b = Xn
4) Erro: [Xn-1 - Xn] < e
Volte ao passo 2

Obs: Xn-1 se refere ao Xn anterior, já que o -1 é referente a 'n'
"""

"""
Método das Cordas (Ou Secante Modificado)
descrição: O objetivo se trata de aproximar dois pontos de um função até conseguir
o valor aproximado da raiz, considerando uma determinada taxa de erro.

Dados de entrada:
    Intervalo [a,b]
    Taxa de erro desejada 'e'
    Função 'f(x)'

1) Se f(a)*f"(a)>0 -> c=a; x0=b : Se existe raiz
   Se f(b)*f"(b)>0 -> c=b; x0=a : Se existe raiz

2) Xn-1 = Xn - [f(Xn) * (Xn-c)] / [f(Xn) - f(c)]
3) Erro: [Xn-1 - Xn] < e
Volte ao passo 2

Obs: Xn-1 se refere ao Xn anterior, já que o -1 é referente a 'n'
"""

"""
Método de Newton Raphson
descrição: O objetivo se trata de aproximar dois pontos de um função até conseguir
o valor aproximado da raiz, considerando uma determinada taxa de erro.

Dados de entrada:
    Intervalo [a,b]
    Taxa de erro desejada 'e'
    Função 'f(x)'

1) Se f(a)*f"(a)>0 -> x0=a : Se existe raiz
   Se f(b)*f"(b)>0 -> x0=b : Se existe raiz

2) Xn-1 = Xn - [f(Xn) / f'(Xn)]
3) Erro: [Xn-1 - Xn] < e
Volte ao passo 2

Obs: Xn-1 se refere ao Xn anterior, já que o -1 é referente a 'n'
"""