import Menu


def printyng():
    id = []
    with open('Note_book.csv', 'r', encoding='utf-8') as file:
        for i in file:
            print(*i.split(' '))
        Menu.restart()





