first_array = [0] * 5
print(len(first_array))
for index in range(0, len(first_array)):
    first_array[index] = int(input(f"Enter values number {index}: "))

sorted_asc = sorted(first_array)
sorted_dsc = sorted(first_array, reverse=True)


print("Ascendingly sorted array = ", sorted_asc)
print("Descendingly sorted array = ", sorted_dsc)
