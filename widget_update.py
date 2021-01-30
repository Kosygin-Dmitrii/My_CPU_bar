#метод не наследуется ни от чего и не импортируется ничего, т.к. используется как модуль, здесь задан метод


class Configure_widgets:                               # Класс, который обновляет значения

    def congifure_cpu_bar(self):                        # Метод для наследования
        r = self.cpu.cpu_percent_return()  # Получаем загрузку каждого потока и записываем ее в переменную
        for i in range(self.cpu.cpu_count_logical):  # Для каждого потока
            self.list_label[i].configure(text=f'core{i + 1} usage :{r[i]}%')  # lsl_label определен в основном файле как пустой список, метод configure сконфигурирует виджет (параметры текст)
            self.list_pbar[i].configure(value=r[i])                          # конфигурация - логическое заполнение места значениями.


        r2 = self.cpu.rum_usage()
        self.ram_lab.configure(text=f'RAMM usage: {r2[2]}%, used{round(r2[3]/1048576)}MB,\n available: {round(r2[1]/1048576)}Mb')
        self.ram_bar.configure(value=r2[2])


        self.wheel = self.after(1000, self.congifure_cpu_bar)             #Метод ткинтера, позволяющий перезапускать данную функцию


    def configure_win(self):
        if self.wm_overrideredirect():
            self.overrideredirect(False)
        else:
            self.overrideredirect(True)
        self.update()
