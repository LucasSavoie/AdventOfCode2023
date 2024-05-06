with open("Real.txt") as f:
    s = f.read()
s = s.split("\n")
r = 0
for x in range(1, len(s) - 2):
    top = s[x - 1]
    cur = s[x]
    bot = s[x + 1]
    for c in range(0, len(cur)):
        if cur[c] == '*':
            first = ""
            sec = ""
            ind = c - 1
            if cur[ind].isdigit():
                while cur[ind].isdigit():
                    first = cur[ind] + first
                    ind -= 1
            ind = c + 1
            if cur[ind].isdigit():
                if first != "":
                    while cur[ind].isdigit():
                        sec = sec + cur[ind]
                        ind += 1
                else:
                    while cur[ind].isdigit():
                        first = first + cur[ind]
                        ind += 1
            temp = ""
            fir = -1
            last = -1
            for i in range(0, len(cur)):
                isGear = False
                if top[i].isdigit():
                    temp += top[i]
                    last = i
                    if fir == -1:
                        fir = i
                if (i == len(cur) - 1 or not top[i].isdigit()) and temp != "":
                    start = fir
                    end = last
                    if fir == 0:
                        start = fir + 1
                    elif end == len(cur) - 1:
                        end = last - 1
                    for j in range(start - 1, end + 2):
                        if j == c:
                            if first == "":
                                first = temp
                            elif sec == "":
                                sec = temp
                    temp = ""
                    fir = -1
                    last = -1
            for i in range(0, len(cur)):
                isGear = False
                if bot[i].isdigit():
                    temp += bot[i]
                    last = i
                    if fir == -1:
                        fir = i
                if (i == len(cur) - 1 or not bot[i].isdigit()) and temp != "":
                    start = fir
                    end = last
                    if fir == 0:
                        start = fir + 1
                    elif end == len(cur) - 1:
                        end = last - 1
                    for j in range(start - 1, end + 2):
                        if j == c:
                            if first == "":
                                first = temp
                            elif sec == "":
                                sec = temp
                    temp = ""
                    fir = -1
                    last = -1
            if first != "" and sec != "":
                print("first: " + first)
                print("seconds: " + sec)
                r += int(first) * int(sec)

print(r)
