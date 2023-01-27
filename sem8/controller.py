import viev

# Создать информационную систему позволяющую работать с учениками школы
# функции
# Добавление нового студента (Поля - имя, фамилия)
# Добавление предмета (добавляется всем ученикам сразу)
# Добавление оценки ученику по предмету (выбираем ученика(из существующих), выбираем предмет(из сущ.),пишем оценку )
# Показ списка учеников (имена фамилия)
# Показ листа оценок конкретного ученика
# Выход из программы
# Достаточно хранить данные в переменной

dict = {}
names = []
lessons = []

def start():
    while True:
        choose = viev.choose()
        if choose == 1:
            name = viev.studets()
            dict[name] = {}
            names.append(name)
            if lessons:
                for les in lessons:
                    dict[name][les] = []
        elif choose == 2:
            lesson = viev.less()
            lessons.append(lesson)
            for nam in names:
                dict[nam][lesson] = []
        elif choose == 3:
            name3, less3, mark3 = viev.mark()
            dict[name3][less3].append(mark3)
        elif choose == 4:
            print(dict.keys())
        elif choose == 5:
            name5 = viev.list()
            print(dict[name5])
        elif choose == 6:
            break
