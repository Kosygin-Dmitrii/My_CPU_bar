import psutil as pt

class CpuBar:

    def __init__(self):
        self.cpu_count = pt.cpu_count(logical=False)         #Выводит количество ядер у процессора (без логических ядер т.е. без потоков)
        self.cpu_count_logical = pt.cpu_count()              #Выводит количество потоков, на каждоя ядре 2 потока.







CpuBar()
