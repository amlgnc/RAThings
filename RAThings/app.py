import json


def printList():
    f = open('RAThings/id-list.json')
    data = json.load(f)
    print(f'{data}\n')
    f.close()

# Main loop
while True:
    print("0: exit\n1: read id-list.json\n")

    option = input()
    if option == '0':
        exit()
    elif option == '1':
        printList()
    else:
        pass