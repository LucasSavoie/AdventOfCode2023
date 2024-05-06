with open("Real.txt") as f:
    s = f.read()
s = s.split("\n")
print(s)
count = 0
r = 0
for x in s:
    first = -1
    last = -1
    cur = ""
    for c in range(0, len(x)):
        if x[c].isdigit():
            cur += x[c]
            last = c
            if first == -1:
                first = c
        if (not x[c].isdigit() or c == len(x) - 1) and cur != "":
            addTo = False
            if count != 0:
                for i in range(first, last + 1):
                    if s[count - 1][i] != '.' and not s[count - 1][i].isdigit():
                        addTo = True
            if count != len(s) - 2:
                for i in range(first, last + 1):
                    if s[count + 1][i] != '.' and not s[count + 1][i].isdigit():
                        addTo = True
            if first != 0:
                top = count - 1
                bot = count + 1
                if count == 0:
                    top = count
                if count == len(s) - 2:
                    bot = count
                for i in range(top, bot + 1):
                    print(s[i][first - 1])
                    if s[i][first - 1] != '.' and not s[i][first - 1].isdigit():
                        addTo = True
                        print(cur)
            if last != len(x) - 1:
                top = count - 1
                bot = count + 1
                if count == 0:
                    top = count
                if count == len(s) - 2:
                    bot = count
                for i in range(top, bot + 1):
                    print(s[i][last + 1])
                    if s[i][last + 1] != '.' and not s[i][last + 1].isdigit():
                        addTo = True
                        print(cur)
            if addTo:
                r += int(cur)
            cur = ""
            first = -1
            last = -1
    count += 1
print(r)
