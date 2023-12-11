ar = [1,8,17,2]
target = 19

# Brute Force , o(n2)
for i in range(len(ar)):
    for j in range(i+1, len(ar)):
        if ar[i]+ar[j]==target:
            print([i,j])
    

# O(n)
newDict = {}
for i in range(len(ar)):
    newValue = target - ar[i]
    if not newValue in newDict:
        newDict[ar[i]]=i
    else:
        print([newDict[newValue], i])


        


