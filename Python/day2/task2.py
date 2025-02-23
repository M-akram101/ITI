length1 = int(input("Enter the length of list1: "))
length2 = length1

key_list = []
value_list = []


for value in range(length1):
    value = input("Enter key: ")
    value1 = input("Enter value: ")
    key_list.append(value)
    value_list.append(value1)

employees_dict = {}
for employee in range(length1):
    employees_dict[key_list[employee]] = value_list[employee]

print("Your Employees Dictionary = ", employees_dict)
