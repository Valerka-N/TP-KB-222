def insert_element(listt, new):
    index_to_insert = len(listt)
    new = str(new)  

    for i, element in enumerate(listt):
        element = str(element)  
        if element >= new:
            index_to_insert = i
            break

    listt.insert(index_to_insert, new)
    return listt

my = [1, 3, 5, 'a', 'c', 'e']
new = input("Введіть новий елемент: ")
my = insert_element(my, new)
print(my)

