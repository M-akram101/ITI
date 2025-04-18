# f = open("/Users/mohamedakram/Desktop/Projects/ITI/Python/day3/file. txt")
# new_list = f.readlines()
# print(new_list)
with open("file.txt") as f:
    content_list = f.readlines()

print(content_list)
