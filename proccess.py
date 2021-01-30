import psutil as pt
####from time import sleep



class CpuBar:

    def __init__(self):
        self.cpu_count = pt.cpu_count(logical=False)         #Выводит количество ядер у процессора (без логических ядер т.е. без потоков)
        self.cpu_count_logical = pt.cpu_count()              #Выводит количество потоков, на каждоя ядре 2 потока.


    def cpu_percent_return(self):                            #Возвращает загрузку процессоров в процентах   (список из 4 значений каждый на ядро)
        return pt.cpu_percent(percpu=True)                   # Percpu-true - возвращает значение по каждому потоку а не общее значение

    def rum_usage(self):                                     # Возвращает использование памяти
        return pt.virtual_memory()                           #Возвращает именнованный кортеж
#svmem(total=12438216704, available=5186166784, percent=58.3, used=6606327808, free=1049608192, active=7835869184, inactive=2783125504, buffers=87822336, cached=4694458368, shared=315187200, slab=552849408)





print(type(CpuBar().rum_usage()))
####x = CpuBar()

####for i in range(10):
####    print(x.cpu_percent_return())
####    sleep(1)                                                #Значения процессора выводятся за промежуток в секунду (среднее значение)                                                                                                                                                           #   df
