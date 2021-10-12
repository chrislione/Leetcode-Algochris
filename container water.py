def maxarea(height):
    ma = 0

    for i in range(len(height)):
        for j in range(1 + i, len(height)):
            area = (j - i) * min(height[i], height[j])
            # print(area)

            ma = max(ma, area)
    return ma


# call function
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
y = maxarea(height)
print(y)