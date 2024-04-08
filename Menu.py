import Create_file
import Delete
import Id
import Note
import Print
import Search
import csv

from replace import Replace


def actionRequest():
    request = input(
        'Какую операцию вы желаете выполнить''\n1-''Поиск''\n2-''Создание''\n3-''Удаление''\n4-''Показать всё''\n5-''Замена значения''\n')
    if request == '1':
        index = input(
            'Пожалуйста введите по какому значению будет происхдить поиск\n1:id\n2:Заголовок\n3:Текст заметки\n4:Дата создания в формате Yan dd yyyy\n')
        search_value = input('Введите искомое значение''\n')
        Search.Search(index, search_value)
        restart()


    elif request == '2':
        id = Id.note_id()
        subject = input('Введите заголовок заметки\n')
        text = input('Введите текст заметки\n')
        note = Note.Note(id, subject, text)
        note.Note_save()
        restart()


    elif request == '3':
        Delete.Delete()

    elif request == '4':
        Print.printyng()

    elif request == '5':
        Replace()

    else:
        restart()


def restart():
    question = input('вы хотите продолжить работать в программе?''\n''yes:Y''\n''no:N''\n')
    if question.upper() == 'Y':
        actionRequest()
    elif question.upper() == 'N':
        print('Goodbye')
        exit()


if __name__ == '__main__':
    Create_file.create()