from scripts.algo import *
import threading as t

N: int = 0


def generatePopulation(cl: Class, size: int, rlist):
    global N
    tables = []
    for i in range(size):
        tables.append(getTimetable(cl))
        print(f"Appended table {i} on pass {N}")
    N += 1
    rlist += tables


def getTablePopulation(cl: Class, size: int = 100, tsize: int = 10):
    ts = []
    tables = []
    for i in range(tsize):
        ts.append(t.Thread(target=generatePopulation,
                  args=(cl, tsize, tables), daemon=True))

    for thr in ts:
        thr.start()

    for thr in ts:
        thr.join()

    return tables
