from Note import *
import csv
import Menu


def Search(index, search_value: str):
    try:
        file = open('Note_book.csv')
    except IOError as e:
        with open('Note_book.csv', 'w', newline='', encoding='UTF-8') as f:
            header = ['id', 'subject', 'text', 'save_data']
            write = csv.writer(f, delimiter=';')
            write.writerow(header)
            print('Файла нет, давай по новой \n')
            Menu.actionRequest()


    else:
        if  str(index).isdigit() == True and int(index) < 3:
            index = int(index) - 1
            with open('Note_book.csv', 'r+', encoding='utf-8') as file:
                data = csv.reader(file, delimiter=';')
                test = []
                for i in data:
                    test.append(i)
                printing = []
                for i in test:
                    if index == 3 and search_value in str(i[index]):
                        printing.append(i)
                    elif i[index] == search_value:

                        printing.append(i)

                if len(printing) == 0:
                    print('Такой записи нет!!! Давай по новой \n')
                    Menu.actionRequest()
                else:
                    for i in printing:
                        print(*i)
                    return printing

        else:
            print('User is imbicil == True\n учись читать')
            Menu.actionRequest()

