def stringop(n):
    a = n
    arr = []
    string = ""
    intval = 0
    length = 0
    arr = a.split()
    for i in arr:
        for j in i:
            length = len(i)
            intval = ord(j) + length
            if intval > 122:
                string = string + "z"
            elif intval > 90 and intval < 96:
                string = string + "Z"
            else:
                string = string + chr(intval)
        string = string + " "
    print(string)


string = "go iNDIa"
stringop(string)

