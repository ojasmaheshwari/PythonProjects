# simple todo list in python
running = True
table: dict = {}

def takeCommand():
    command: str = input("Command> ")
    return command

def addEntry(data: list):
    if len(data) % 2 == 0:
        for i in range(len(data)):
            if i % 2 == 0:
                table[data[i]] = data[i+1]
    else:
        print("Data to be inserted is in an invalid format")
        return

def deleteEntry(data: list):
    table_keys = table.keys()
    for d in data:
        if d in table_keys:
            print(f"Deleting {d} in table")
            table.pop(d)
        else:
            print(f"{d} not found in table, skipping")

def showTable():
    for key, value in table.items():
        print(key, value)

def processCommand(command: str):
    cmd_prefix: str = str(command.split(' ')[0])
    data: list = command.split(' ')[1:]
    match cmd_prefix:
        case "add":
            addEntry(data)
        case "del":
            deleteEntry(data)
        case "show":
            showTable()
        case "exit":
            global running
            running = False
        case _:
            print("Invalid command")

while running:
    command: str = takeCommand()
    processCommand(command)

