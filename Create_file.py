import csv

import Menu


def create():
    try:
        file = open('Note_book.csv')
    except IOError as e:
        with open('Note_book.csv', 'w', newline='', encoding='UTF-8') as f:
            header = ['id', 'subject', 'text', 'save_data']
            write = csv.writer(f, delimiter=';')
            write.writerow(header)

    Menu.actionRequest()