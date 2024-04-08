import Search
import Note
import csv
import Menu


def Replace():
    try:
        index = input('Что вы желаете заменить \n1:Заголовок\n2:Текст заметки')
        value = input('Введите искомое значение')
        if index == 1:
            data_value = 'заголовок'
            hard = index
            replaceing(value, int(index), data_value,hard)
        else:
            data_value = 'текст заметки'
            hard = index
            replaceing(value, int(index), data_value,int(hard))
    except ValueError as e:
        print('Пиши цифры а не буквы!\nCмотри приме в МЕНЮ!!!!')
        Menu.restart()


def replaceing(value: str, index: int, data_value: str,hard_index:int):
    try:
        old_value = Search.Search(index, value)
        if len(old_value) > 1:
            print('Найдено несколько значений')
            for i in old_value:
                print(*i)
                index =0
            ex = input('Введите id изменяемого объекта')
            replaceing(ex, index, data_value,hard_index)
        else:
            re = input(f'Введите новый {data_value}')
            with open('Note_book.csv', 'r', encoding='utf-8') as file:
                data = file.read()

                a = old_value[0].copy()

                a[hard_index] = re

                new_value = str(Note.Note(a[0], a[1], a[2]))


                data = data.replace(';'.join(old_value[0]), new_value)
            with open("Note_book.csv", "w", encoding='utf-8') as file:
                file.write(data)
                Menu.restart()
    except ValueError as e:
        print('Пиши цифры а не буквы!\nCмотри приме в МЕНЮ!!!!')
        Menu.restart()
