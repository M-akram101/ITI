def longest_sub():
    charSet = set()
    word = input("enter")
    l = 0
    res = 0
    for r in range(len(word)):
        print(charSet)
        while word[r] in charSet:
            charSet.remove(word[l])
            l += 1
        charSet.add(word[r])
        res = max(res, r - 1 + 1)
    return res


print(longest_sub())
