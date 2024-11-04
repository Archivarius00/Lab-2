from csv import reader


cnt = 0

with open('books-en.csv', 'r') as list_book:
    file = reader(list_book, delimiter=';')
    for row in file:
        if len(row[1]) > 30:
            cnt += 1

print(f"Подходящие по условию книги: {cnt}")