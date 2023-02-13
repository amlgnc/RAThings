import json
import webbrowser


def printHelp():
    print("")
    print("exit      : exit the console application                    :")
    print("help      : show help                                       :")
    print("list      : show 'id-list.json'                             :")
    print("check     : open the jr. developer review requests web page :")
    print("game <id> : open the game web page                          :")
    print("          : <id> : the retroachievements.org game id        :")


def printList():
    f = open('RAThings/id-list.json')
    data = json.load(f)
    print(f'{data}')
    f.close()


def openChecklistWebPage():
    webbrowser.open("https://docs.google.com/spreadsheets/d/e/2PACX-1vSl4tRG-wV1lxtb-2ZJYRoM0VLnQPYoQO1jOVRmb8TFWldFJGr7RrO6-I-c6rWK0XsZ1h5pJEOStjmQ/pubhtml?gid=1582422742&single=true")


def openGameWebPage(cmd):
    parts = cmd.split()
    if parts[0] == "game":
        webbrowser.open(f'https://retroachievements.org/game/{parts[1]}')
    else:
        print("invalid command")


def interpreter(cmd):
    if cmd == "exit":
        exit()
    elif cmd == "help":
        printHelp()
    elif cmd == "list":
        printList()
    elif cmd == "check":
        openChecklistWebPage()
    elif cmd.find("game") != -1:
        openGameWebPage(cmd)
    else:
        print("invalid command")


# Main loop
while True:
    interpreter(input())
    print("")
