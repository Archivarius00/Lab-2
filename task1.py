# книги, более 30 символов
from csv import reader


count = 0

with open('books-en.csv', 'r') as list_book:
    file = reader(list_book, delimiter=';')
    for row in file:
        if len(row[1]) > 30:
            count += 1

print(f"Подходящие по условие книги: {count}")