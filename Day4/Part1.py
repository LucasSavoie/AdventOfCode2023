with open("Real.txt") as f:
    s = f.read()
s = s.split("\n")
s.pop()
r = 0
for x in s:
    nums = x.split(":")[1]
    myNums, winNums = nums.split("|")
    myNums = myNums.split(" ")
    winNums = winNums.split(" ")
    cur = 0
    winNums = list(filter(lambda x: x != "", winNums))
    myNums = list(filter(lambda x: x != "", myNums))
    print(myNums)
    print(winNums)
    for x in myNums:
        if x in winNums:
            print(x)
            if cur == 0:
                cur = 1
            else:
                cur = cur * 2
    r += cur
print(r)
