from csv import reader


def convert(item):
    if item.count(',') == 0:
        return int(item)
    else:
        item = item.replace(',','.')
        return float(item)


arr = []

autor = input('Type author name: ')
autor = autor.lower()

with open('books-en.csv', 'r') as list_book:
    file = reader(list_book, delimiter=';')
    for row in file:
        if (row[2]).lower() == autor:
            if convert(row[6]) >= 0:
                arr.append(row[1])


if __name__ == "__main__":
    if arr == []:
        print('No books have been found')
    else:
        for i in arr:
            print(i)




