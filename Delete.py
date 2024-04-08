import Menu
import Note
import Search
import csv


def Delete():
    index = input('По какому значению будет произведён поиск? \n1:Заголовок\n2:Текст заметки\n')
    delete_value = input('Введите значение которое желаете удалить\n')
    try:
        delete = Search.Search(int(index),delete_value)
        if len(delete) > 1:
            ex = 0
            for i in delete:
                print(*i)
            delete_value = input('Введите id изменяемого объекта\n')

            delet(int(ex), str(delete_value))
        else:
            delet(int(index), str(delete_value))
    except ValueError as e:
        print('Пиши цифры а не буквы!\nCмотри приме в МЕНЮ!!!!')
        Menu.restart()




def delet(ex,delete):
        with open("Note_book.csv", 'r+',encoding='utf-8') as file:
            value_to_delete = Search.Search(int(ex),delete)
            a = ";".join(value_to_delete[0])+'\n'
            data = file.readlines()

            lines = []
            for i in data:
                if i != a:
                    lines.append(i)

            with open("Note_book.csv", "w", encoding='utf-8') as file:

                for i in lines:
                    file.write(i)
                print('Удаление произошло')
            Menu.restart()


