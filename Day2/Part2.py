with open("Real.txt") as f:
    s = f.read()


sum = 0
for x in s.strip().split("\n"):
    x = x.split(":")
    gameNum = int(x[0].split(" ")[1])
    print(gameNum)
    games = x[1].split(";")
    canBe = True
    maxBlue = 0
    maxRed = 0
    maxGreen = 0
    for ss in games:
        cur = ss.split(",")
        print(cur)
        for g in cur:
            if canBe is False:
                break
            g = g[1::]
            num = ""
            for w in g:
                if w == " ":
                    break
                else:
                    num += w
            color = g[len(num) + 1::]
            num = int(num)
            if color == "red" and num > maxRed:
                maxRed = num
            elif color == "blue" and num > maxBlue:
                maxBlue = num
            elif color == "green" and num > maxGreen:
                maxGreen = num
    print(maxBlue * maxRed * maxGreen)
    if canBe:
        sum += maxGreen * maxBlue * maxRed
print(sum)
