a = "bcbaaaaaab"
b = "bcaaaaaab"
hashM = {}
for i in range(len(a)):

    if a[i] in hashM:
        hashM[a[i]] += 1
        continue
    hashM[a[i]] = 1

for i in range(len(b)):
    if b[i] in hashM:
        hashM[b[i]] -= 1
        if hashM[b[i]] == 0:
            del hashM[b[i]]

extra_char = list(hashM)
print("This is the extra character in the two strings", extra_char[0])
