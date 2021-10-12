def binarySearch(listz, target):
    listz.sort(reverse=False) #sort from lowest to highest Ascending order you can also use .sort()
    first=0
    last=len(listz)-1
    while first <= last:
        midpoint = (first+last)//2
        if target == listz[midpoint]:
            return "found at index position" + " "+ str(midpoint)
        elif listz[midpoint] < target:
            first = midpoint+1
        else:
            last = midpoint-1
    return None
    #check
listx = [1,5,9,12,2]
target=12
x=binarySearch(listx, target)
print(x)