# "pwjkewjja"
# "paewkltz"
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
# Example 4:
#
# Input: s = ""
# Output: 0
# class Solution(object):
def lengthOfLongestSubstring(lists):
    lists = (list(lists))  # work with this

    # print(lists)
    newlist = []
    mymemory = []
    k = 0
    x = 0
    y = 0

    if not lists:
        print("list is empty")
        newlist = [0]
        # print(lists)
    else:

        while x <= len(lists) - 1:
            if lists[x] in mymemory:
                # print(mymemory)
                k = len(mymemory)
                newlist.append(k)
                mymemory = []
                y = y + 1
                x = y

                # print(k)
            elif lists[x] not in mymemory:
                mymemory.append(lists[x])
                z = len(mymemory)
                newlist.append(z)
                # mymemory=[]

                x = x + 1

    return (max(newlist))


# call function
lists = "rtttyhnbgrbgf"
result = lengthOfLongestSubstring(lists)
print(result)


