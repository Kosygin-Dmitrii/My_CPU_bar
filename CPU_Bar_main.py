import tkinter as tk
from tkinter import ttk         # Моудль для нового вида виджетов с оформлением WINDOW
import sys
from proccess import CpuBar
from widget_update import Configure_widgets



geom = '400x400'
class Application(tk.Tk, Configure_widgets):           #Наследуемся от класса создания основного окна
    def __init__(self):             # Перегружаем метод инит у класса
        tk.Tk.__init__(self)
        self.geometry(geom)            # Создание геометрии окна  400x400+50+1000 - ширина высота и отступы от угла
        self.attributes('-alpha', 1)            # Прозрачнотсь

        self.attributes('-topmost', True)       # Поверх всех окон или нет
        self.overrideredirect(False)         #Если тру, то удаляет всю рамку виджета(закрыть свернуть)
        self.resizable(False, False)        # При фолз запрещает изменять размерность окна
        self.title('My_CPU_BAR')           #Панель названия окна


        self.cpu = CpuBar()         #Определяем метод вызывающий класс,отражающий ядра, созданный в отдельном модуле.
        self.run_set_ui()


    def run_set_ui(self):
        self.set_ui()               #Инициализируем окно и запускаем свой метод, который заполнит окно нашими параметрами
        self.make_bar_cpu_usage()   #Заполняет окно виджетами
        self.congifure_cpu_bar()    # Конфигурирует значения в ввиджеты, т.к. наследовался класс приложение от виджет_апдейт, то берем от туда этот метод


    def set_ui(self):               # Набор графических ВИДЖЕТОВ для интерфейса на главном окне
        exit_but = ttk.Button(self, text='Exit', command=self.app_exit)        #Создание кнопки с названием,  command- команда иполняемая по нажатию, это метод класса с названием app_exit
        exit_but.pack(fill=tk.X)                #метод - УПАКОВЩИК pack()-сверху по центру (grid, place)  fill(заполнение) растягивает по Х

        self.bar2 = ttk.LabelFrame(self, text='manual')                   # Frame -Class - создание рамки для размещения виджетов
        self.bar2.pack(fill=tk.X)

        self.combo_win = ttk.Combobox(self.bar2, value=['hide',"don't hide",'min'],state='readonly',width=9)    # Combobox-выпадающий список размещаем на фрейме бар2, передаем значения из выпадающего меню и только для чтения в список
        self.combo_win.current(1)    # Выбираем значение из выпадающего меню по умолчанию (текущее) из списка value по индексу
        self.combo_win.pack(side=tk.LEFT)



        ttk.Button(self.bar2, text='Move', command=self.configure_win).pack(side=tk.LEFT)              # Создаем кнопку, размещаем на фрейме бар2, side - сторона
        ttk.Button(self.bar2, text='>>>').pack(side=tk.LEFT)

        self.bar1 = ttk.LabelFrame(self, text='Power')
        self.bar1.pack(fill=tk.BOTH)            #выравнивание по ширине
        self.test = ttk.Button(self.bar2, text='test').pack(side=tk.LEFT)


        self.bind_class('Tk', '<Enter>',self.enter_mouse)     #Позволяет сделать окно появляющимся bind - jбрабатывает события наведения нажатия и прочее. При наведение на класс-Tk. Будут вызываться методы
        self.bind_class('Tk', '<Leave>',self.leave_mouse)     #Enter - при наведении мыши Leave - при покидании

        self.combo_win.bind('<<ComboboxSelected>>',self.choise_combo)    #При выборе пунктов используем метод сомбо чойз

    def make_bar_cpu_usage(self):
        ttk.Label(self.bar1, text=f'physical_cores: {self.cpu.cpu_count}, logical cores:{self.cpu.cpu_count_logical}',       #lable  - метка(название, шапка) на фрейме Power
                  anchor=tk.CENTER).pack(fill=tk.X)     #anchor - якорь прикрепляем как метку к ередине экрана и устанавливаем по ширине

        self.list_label = []    #
        self.list_pbar = []     #Прогресс бар

        for i in range(self.cpu.cpu_count_logical):             #по количеству потоков создаем списки
            self.list_label.append(ttk.Label(self.bar1, anchor=tk.CENTER))
            self.list_pbar.append(ttk.Progressbar(self.bar1, length=100))       #длина будет разбита на 100 делений (под % загрузку процессора)

        for i in range(self.cpu.cpu_count_logical):
            self.list_label[i].pack(fill=tk.X)
            self.list_pbar[i].pack(fill=tk.X)

        self.ram_lab = ttk.Label(self.bar1,  anchor=tk.CENTER)           #создаем метку для оперативной памяти по центру
        self.ram_lab.pack(fill=tk.X)                                                #Заполняем растягиваем по Х
        self.ram_bar = ttk.Progressbar(self.bar1, length=100)                       #Создаем шкалу на 100 делений
        self.ram_bar.pack(fill=tk.X)                                                #Растягиваем по Х

    def make_minimal_win(self):                                             # Заполнение окна виджетами в минимальном режиме
        self.bar_one = ttk.Progressbar(self, length=100)
        self.bar_one.pack(side=tk.LEFT)

        self.ram_bar = ttk.Progressbar(self, length=100)
        self.ram_bar.pack(side=tk.LEFT)

        ttk.Button(self, text='full', command=self.make_full_win,width=5).pack(side=tk.LEFT)
        ttk.Button(self, text='move', command=self.configure_win, width=5).pack(side=tk.LEFT)

        self.geometry('')

        self.update()
        self.configure_minimal_win()


    def enter_mouse(self,event):     #Метод при наведении мыши, event - обязательно указатьб при срабатвывании оброботчика ошибок
        if self.combo_win.current() == 0 or 1: #Если выбрано значение из списка скрывать или не скрывать
            self.geometry(geom)     #Геометрия окна будет оставаться по умолчанию, такая какая есть


    def leave_mouse(self,event):
        if self.combo_win.current() == 0:
           self.geometry(f'{self.winfo_width()}x20')   # получаем текущее значение размеров окна и меняем его, если выбран пункт 1 - свернуть приложение


    def choise_combo(self, event):                 #Срабатывает при выборе любого метода из бокса
        if self.combo_win.current() == 2:   # Выбран пункт min
            self.enter_mouse('')            # Пустая строка нужна чтобы в евент что-то попало(он обязателен)
            self.unbind_class('Tk','<Enter>')   #отвязываем событие при наведении мыши на окно
            self.unbind_class('Tk','<Leave>')
            self.combo_win.unbind('ComboboxSelected>>')    # Отвязываем событие выбора пунктов из сомбобокса
            self.after_cancel(self.wheel)                   # Обрываем процесс, перезапускающий функцию получения данных от процессора данные из ядер
            self.clear_win()                                # вызываем метод очищающий окно
            self.update()
            self.make_minimal_win()


    def make_full_win(self):            # Заполнение ркна при переходе в фул режим
        self.after_cancel(self.wheel)   # Остановили процесс обновления получения значений от cpu
        self.clear_win()                # очистили окно от виджетов
        self.update()
        self.run_set_ui()               # Запускаем прорисовку главного окна


    def app_exit(self):             # Метод класса
        self.quit()
        sys.exit()                  #Убить процесс



if __name__ == '__main__':
    root = Application ()               # Создание базового окна в функцоинальном стиле
    root.mainloop()