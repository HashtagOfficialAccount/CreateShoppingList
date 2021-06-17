print('Hello and welcome to your shopping list!')
print('When you are done with all the items, type done to finish!')
list = []
def add():
    item = input('Enter the item you want to add to your list: ')
    list.append(item)
    while item == 'done':
        list.pop()
        print('Here is your shopping list: ',list)
        print('Have a good day shopping!')
        break
    else: 
        add()
add()
