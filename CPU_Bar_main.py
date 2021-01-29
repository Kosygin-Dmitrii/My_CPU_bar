import tkinter as tk
from tkinter import ttk         # Моудль для нового вида виджетов с оформлением WINDOW
import sys

geom = '400x400'
class Application(tk.Tk):           #Наследуемся от класса создания основного окна
    def __init__(self):             # Перегружаем метод инит у класса
        tk.Tk.__init__(self)
        self.geometry(geom)            # Создание геометрии окна  400x400+50+1000 - ширина высота и отступы от угла
        self.attributes('-alpha', 1)            # Прозрачнотсь

        self.attributes('-topmost', True)       # Поверх всех окон или нет
        self.overrideredirect(False)         #Если тру, то удаляет всю рамку виджета(закрыть свернуть)
        self.resizable(False, False)        # При фолз запрещает изменять размерность окна
        self.title('My_CPU_BAR')           #Панель названия окна

        self.set_ui()               #Инициализируем окно и запускаем свой метод, который заполнит окно нашими параметрами


    def set_ui(self):               # Набор графических ВИДЖЕТОВ для интерфейса
        exit_but = ttk.Button(self, text='Exit', command=self.app_exit)        #Создание кнопки с названием,  command- команда иполняемая по нажатию, это метод класса с названием app_exit
        exit_but.pack(fill=tk.X)                #метод - УПАКОВЩИК pack()-сверху по центру (grid, place)  fill(заполнение) растягивает по Х

        self.bar2 = ttk.LabelFrame(self, text='manual')                   # Frame -Class - создание рамки для размещения виджетов
        self.bar2.pack(fill=tk.X)

        self.combo_win = ttk.Combobox(self.bar2, value=['hide',"don't hide",'min'],state='readonly',width=9)    # Combobox-выпадающий список размещаем на фрейме бар2, передаем значения из выпадающего меню и только для чтения в список
        self.combo_win.current(1)    # Выбираем значение из выпадающего меню по умолчанию (текущее) из списка value по индексу
        self.combo_win.pack(side=tk.LEFT)



        ttk.Button(self.bar2, text='Move').pack(side=tk.LEFT)              # Создаем кнопку, размещаем на фрейме бар2, side - сторона
        ttk.Button(self.bar2, text='>>>').pack(side=tk.LEFT)

        self.bar2 = ttk.LabelFrame(self, text='Power')
        self.bar2.pack(fill=tk.BOTH)            #выравнивание по ширине
        self.test = ttk.Button(self.bar2, text='test').pack(side=tk.LEFT)


        self.bind_class('Tk', '<Enter>',self.enter_mouse)     #Позволяет сделать окно появляющимся bind - jбрабатывает события наведения нажатия и прочее. При наведение на класс-Tk. Будут вызываться методы
        self.bind_class('Tk', '<Leave>',self.leave_mouse)     #Enter - при наведении мыши Leave - при покидании

    def enter_mouse(self,event):     #Метод при наведении мыши, event - обязательно указатьб при срабатвывании оброботчика ошибок
        if self.combo_win.current() == 0 or 1: #Если выбрано значение из списка скрывать или не скрывать
            self.geometry(geom)     #Геометрия окна будет оставаться по умолчанию, такая какая есть


    def leave_mouse(self,event):
        if self.combo_win.current() == 0:
           self.geometry(f'{self.winfo_width()}x20')   # получаем текущее значение размеров окна и меняем его, если выбран пункт 1 - свернуть приложение



    def app_exit(self):             # Метод класса
        self.quit()
        sys.exit()                  #Убить процесс




root = Application ()               # Создание базового окна в функцоинальном стиле
root.mainloop()