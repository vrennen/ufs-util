import os
import json


with open('notas.json', 'rt') as notas:
    disciplinas = json.load(notas)
periodosConcluidos = 4
CHMedia = 3810 / 10


def calcMC():
    notasPonderadas = cargaAcumulada = 0
    for i in disciplinas.values():
        notasPonderadas += i[0] * i[1]
        cargaAcumulada += i[1]
    return round(notasPonderadas / cargaAcumulada, 2)


def calcIECH():
    CHAprovada = CHUtilizada = 0
    for i in disciplinas.values():
        CHUtilizada += i[1]
        if i[0] >= 5.0:
            CHAprovada += i[1]
    return round(CHAprovada / CHUtilizada, 3)


def calcIEPL():
    CHEsperada = CHMedia * periodosConcluidos
    CHAcumulada = 0
    for i in disciplinas.values():
        if i[0] >= 5.0:
            CHAcumulada += i[1]
    return round(CHAcumulada / CHEsperada, 3)


def calcIEA():
    return round(calcMC() * calcIECH() * calcIEPL(), 4)


def main():
    print(f"Media de Conclusão:                       {calcMC()}")
    print(f"Indice de Eficiencia em Carga Horaria:    {calcIECH()}")
    print(f"Indice de Eficiencia em Periodos Letivos: {calcIEPL()}")
    print(f"Indice de Eficiencia Academica:           {calcIEA()}")


if __name__ == "__main__":
    main()
    os.system("pause")
