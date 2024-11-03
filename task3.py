import random
from csv import reader


document = open("task3.txt", "w")


res_cnt = 0
random_cnt = 0
random_array = [random.randint(1, 9410) for _ in range(20)]

with open('books-en.csv', 'r') as list_book:
    file = reader(list_book, delimiter=';')
    for row in file:
        res_cnt+=1
        if res_cnt in random_array:
            random_cnt += 1
            document.write( f"{random_cnt}) {row[2]}. {row[1]} - {row[3]}" + '\n')

document.close()
            
            

if __name__ == "__main__":
    print('List has been generated')
    