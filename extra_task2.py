import heapq
from csv import reader

cnt = 0
nums = []
n = 1

with open('books-en.csv', 'r') as list_book:
    file = reader(list_book, delimiter=';')
    for row in file:
        if cnt != 0:
            nums.append(row[5])
        cnt+=1



if __name__ == "__main__": 

    for i in range(len(nums)):
        nums[i] = int(nums[i])

    nums.sort()
    nums = nums[-20:]
    
    for i in range(len(nums)):
        nums[i] = str(nums[i])


    print('20 самых популярных книг:') 
    with open('books-en.csv', 'r') as list_book:
        file = reader(list_book, delimiter=';')
        for row in file:
            if n <= 20:
                if row[5] in nums:
                    print( f"{n}) {row[1]}" )
                    n += 1
            else: 
                exit()





        

