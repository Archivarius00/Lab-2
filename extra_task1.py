from csv import reader


cnt = 0
arr = []


with open('books-en.csv', 'r') as list_book:
    file = reader(list_book, delimiter=';')
    for row in file:
        cnt+=1
        if cnt != 1:
            arr.append(row[4])


if __name__ == "__main__":
    result = []

    for num in arr:
        if num not in result:
            result.append(num)
    print('Вот все издатели, присутвующие в данном перечне:')
    print(*result, sep = '; ')

