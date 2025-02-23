list_of_nums = []
for number in range(4):
    list_of_nums.append(int(input("Please enter a number: ")))

list_of_nums.pop()
list_of_nums.insert(2, "R")

num_from_user = int(input("Please enter a number"))

list_of_nums.remove(num_from_user)
print("this is the last version for your list: ", list_of_nums)
