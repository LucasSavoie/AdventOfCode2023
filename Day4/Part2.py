with open("Real.txt") as f:
    s = f.read()
s = s.split("\n")
s.pop()
r = 0
cardsNum = [1] * len(s)
ind = 0
for x in s:
    nums = x.split(":")[1]
    myNums, winNums = nums.split("|")
    myNums = myNums.split(" ")
    winNums = winNums.split(" ")
    cur = 0
    winNums = list(filter(lambda x: x != "", winNums))
    myNums = list(filter(lambda x: x != "", myNums))
    for x in myNums:
        if x in winNums:
            cur += 1
    for x in range(0, cardsNum[ind]):
        for i in range(ind + 1, 1 + ind + cur):
            if i < len(cardsNum):
                cardsNum[i] += 1
    ind += 1
print(sum(cardsNum))
