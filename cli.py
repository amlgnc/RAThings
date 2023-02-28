import webbrowser


def openChecklistWebPage():
    webbrowser.open('https://docs.google.com/spreadsheets/d/e/2PACX-1vSl4tRG-wV1lxtb-2ZJYRoM0VLnQPYoQO1jOVRmb8TFWldFJGr7RrO6-I-c6rWK0XsZ1h5pJEOStjmQ/pubhtml?gid=1582422742&single=true')


def openGameWebPage(cmd):
    parts = cmd.split()
    if parts[0] == 'game':
        webbrowser.open(f'https://retroachievements.org/game/{parts[1]}')
    else:
        print("\nNo.")


# Main loop
while True:
    cmd = input()
    if cmd == 'exit':
        exit()
    elif cmd == 'check':
        openChecklistWebPage()
    elif cmd.find('game') != -1:
        openGameWebPage(cmd)
    else:
        print("\nNo.")
    print('')
