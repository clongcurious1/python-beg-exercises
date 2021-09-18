def banner(message, border = '-'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)

banner("Hot Dog Eating Contest")

banner ("Blue Ribbon Recipe Contest", "*")

