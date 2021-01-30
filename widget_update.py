#метод не наследуется ни от чего и не импортируется ничего, т.к. используется как модуль, здесь задан метод


class Configure_widgets:                               # Класс, который обновляет значения

    def congifure_cpu_bar(self):                        # Метод для наследования
        r = self.cpu.cpu_percent_return()  # Получаем загрузку каждого потока и записываем ее в переменную
        for i in range(self.cpu.cpu_count_logical):  # Для каждого потока
            self.list_label[i].configure(text=f'core{i + 1} usage :{r[i]}%')  # lsl_label определен в основном файле как пустой список, метод configure сконфигурирует виджет (параметры текст)
            self.list_pbar[i].configure(value=r[i])                          # конфигурация - логическое заполнение места значениями.


        r2 = self.cpu.ram_usage()
        self.ram_lab.configure(text=f'RAMM usage: {r2[2]}%, used{round(r2[3]/1048576)}MB,\n available: {round(r2[1]/1048576)}Mb')
        self.ram_bar.configure(value=r2[2])


        self.wheel = self.after(1000, self.congifure_cpu_bar)             #Метод ткинтера, позволяющий перезапускать данную функцию


    def configure_win(self):
        if self.wm_overrideredirect():
            self.overrideredirect(False)
        else:
            self.overrideredirect(True)
        self.update()


    def clear_win(self):                      # Очищение окна от виджетов для min режима
        for i in self.winfo_children():            # Возвращает список виджетов размещенных на главном окне
            print(i)
            i.destroy()


    def configure_minimal_win(self):                                        # заполняем шкалы в минимальном режиме
        self.bar_one.configure(value=self.cpu.cpu_one_return())             # Общая загрузка ядер
        self.ram_bar.configure(value=self.cpu.ram_usage()[2])               # Занятость ОЗУ
        self.wheel = self.after(1000, self.configure_minimal_win)