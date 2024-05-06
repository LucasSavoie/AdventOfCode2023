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
while True:
    cur = f.readline()
    print(cur)
    if len(cur) == 0:
        f.close()
        break
    firstInt = None
    secondInt = None
    for x in cur:
        if x.isdigit():
            secondInt = int(x)
            if firstInt is None:
                firstInt = int(x)
    print(firstInt * 10 + secondInt)
    sum += firstInt * 10 + secondInt
print(sum)
