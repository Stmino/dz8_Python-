
def choose():
    choose = int(input('Выберите действие(введите цифру):\n\
              1- Добавление нового студента (Поля - имя, фамилия)\n\
              2- Добавление предмета (добавляется всем ученикам сразу)\n\
              3- Добавление оценки ученику по предмету (выбираем ученика(из существующих),\n\
                 выбираем предмет(из сущ.),пишем оценку)\n\
              4- Показ списка учеников (имена фамилия)\n\
              5- Показ листа оценок конкретного ученика\n\
              6- Выход из программы\n\
                 Введите цифру:'))
    return choose


def studets():
    name1 = input('Введите Имя:  ')
    name2 = input('Введите Фамилию:  ')
    name = name1+' '+name2
    return name


def less():
    lesson = input('ВВедите название предмета:')
    return lesson


def mark():
    name3_1 = input('Введите Имя студента: ')
    name3_2 = input('Введите Фамилию студента: ')
    name3=name3_1+' '+name3_2
    less3 = input('Введите предмет: ')
    mark3 = input('Веедите оценку: ')
    return name3, less3, mark3


def list():
    name5_1 = input('Введите Имя  студента: ')
    name5_2 = input('Фамилию студента: ')
    name5=name5_1+' '+name5_2
    return name5
