close = False
p1 = None
p2 = None
totalp = None

while not close:

    print("\nPoint Duo"
          "\n1.Definir p1"
          "\n2.Definir p2"
          "\n3.Definir total de pontos equidistante"
          "\n4.Encontrar"
          "\n5.sair")

    choise = str(input("->"))

    if choise == '1':
        p1 = float(input("Digite o primeiro ponto: "))
    elif choise == '2':
        p2 = float(input("Digite o segundo ponto: "))
    elif choise == '3':
        totalp = int(input("Digite o total de pontos buscados: ")) - 1
    elif choise == '4':
        if p1 is None or p2 is None or totalp is None:
            print("Dados não informados!")
        elif p1 == p2:
            print("Os pontos são o mesmos!")
        else:
            if p1 > p2:
                save = p1
                p1 = p2
                p2 = save

            vetor = [0]
            size: float = ((p2 - p1) / totalp)

            print(p1, p2, size)

            pointvar: float = p1
            while pointvar < p2:
                pointvar = pointvar + size
                vetor.append(pointvar)

            print(vetor)
    elif choise == '5':
        close = True
