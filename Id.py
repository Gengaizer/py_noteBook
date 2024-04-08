
def note_id():
    id = []
    with open('Note_book.csv', 'r', encoding='utf-8') as file:
        for i in file:
            a = list(i.split(';'))
            if a[0].isdigit():
                id.append(int(a[0]))


        id = sorted(id)
        count = 0
        if len(id)<=0:
            return 1
        for i in id:
            count += 1
            if int(i) == count:
                pass
            else:
                return count
        if int(id[-1]) == count:
            count+=1
            print(count)
            return count


