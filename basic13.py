#print 1-255
for idx in range(1,255):
    print idx

#print ints and sum 0-255
sm = 0
for idx in range(0,255):
    print idx
    sm += idx
    print sm
#find and print max
arr = [1,2,3,4,5]
mx = arr[0]
for idx in arr:
    if idx > mx:
        mx = idx
print mx

#array with odds
oddArr = []
for idx in range(1, 255, 2):
    oddArr.append(idx)
print oddArr
#Greater than Y
arr = [2,3,4,5,6,7,8]
y = 5
count = 0
for idx in arr:
    if idx == y:
        count += 1
        print idx
print count
#max, min, avg
mmaArr = [43,43,43,4,3,2,3,26,6,22,1,2,3,67,2]
nMax = mmaArr[0]
nMin = mmaArr[0]
nSum = 0
for iii in mmaArr:
    if nMax < iii:
        nMax = iii
    if nMin > iii:
        nMin = iii
    nSum += iii
print nMax
print nMin
print nSum/len(mmaArr)
#Swap String for array Negative Values
aArr = [-1,5,-6,5,8,-7,7,8,9,5,-3]
string = "Dojo"
for idx in aArr:
    if idx < 0:
        idx = string
print aArr

#print odds 1-255
for iii in range(1,255,2):
    print iii

#iterate and print array
iArr = [8,6,7,5,75,6]
for idx in iArr:
    print idx

#get and print average
nArr = [43,5,5,2,26,6,6,4,2,2,2,3,34,6,6,7,555]
gsum = 0
for iii in nArr:
    gsum += iii
print gsum/len(nArr)

#Square the Values
sArr = [2,5,48,78,6,3,24]
for idx in sArr:
    idx *= idx
print sArr

#zero out negative numbers
mArr = [-5, -6, 4, 5, -101010, 5, 3, -7, 98]
for iii in mArr:
    if iii < 0:
        iii = 0
print mArr

#Shift Array Values
shArr = [5,7,84,6,84,3,5]
temp = 0
for idx in range(0,len(shArr)):
    shArr[idx-1] = shArr[idx]
shArr[len(shArr)-1]=0
print shArr






















