f = open("Real.txt", "r")
sum = 0
myDict = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9
}

checker = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "zero": 0
}
while True:
    cur = f.readline()
    print(cur)
    if len(cur) == 0:
        f.close()
        break
    firstInt = None
    secondInt = None
    s = ""
    for x in cur:
        s += x
        if x.isdigit():
            secondInt = int(x)
            if firstInt is None:
                firstInt = int(x)
        else:
            for y in checker:
                if s.endswith(y):
                    secondInt = checker[y]
                    if firstInt is None:
                        firstInt = checker[y]
    print(firstInt * 10 + secondInt)
    sum += firstInt * 10 + secondInt
print(sum)
