items =["milk", "bread", "eggs"]
def add_item():
    items.append("jam")
    print(items)
def remove_last_item():
    items.pop()
    print(items)
add_item()
remove_last_item()
item= lambda x:print("item:",x)
for x in items:
    item(x)
def sum_characters(item,index=0):
    if index == len(item):
        return 0
    else:
        return len(item[index])+sum_characters(item,index +1)
print(f"total number of characters in the list is {sum_characters(items)}")