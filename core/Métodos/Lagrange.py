xs: list = []
ys: list = []

totalpontos = int(input(f"Insira total de pontos"))
valorprocurado = int(input(f"Insira valor procurado"))

for i in range(totalpontos):
    xs.append(float(input(f"Insira x{i}")))

for i in range(totalpontos):
    ys.append(float(input(f"Insira y{i}")))


def L(xs, totalpontos, k, valorx):
    result: float = 1
    for j in range(totalpontos):
        if j != k:
            result = result * (valorx - xs[j])/(xs[k] - xs[j])
    return result

def P(ys, totalpontos, valorprocurado):
    result: float = 0
    for k in range(totalpontos):
        result += ys[k] * L(xs, totalpontos, k, valorprocurado)
    return result

print(P(ys, totalpontos, valorprocurado))