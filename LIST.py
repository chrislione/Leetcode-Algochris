def linear_search(lists, target):
    size = len(lists)
    for i in range(size):
        # so lists[0]=1 lists[1]=2 etc..
        if lists[i] == target:
            return "The number" + " " + str(lists[i]) +" " + "was found in index"+" "+ str(i)
    return None


# call function
lists = [10, 20, 30, 40, 50]
target_element = int(input("enter number to search:"))
linear = linear_search(lists, target_element)
print(linear)