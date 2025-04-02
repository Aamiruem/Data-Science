nested_list = [[1, 2], [3, 4], [5, 6]]  # List of lists

print(nested_list)  # [[1, 2], [3, 4], [5, 6]]
print(nested_list[0])  # [1, 2]
print(nested_list[0][0])  # 1

nested_list[0][0] = 0  # Modifying the value at index (0, 0)

print(nested_list)  # [[0, 2], [3, 4], [5, 6]]

nested_list.append([7, 8])  # Adding a new sublist

print(nested_list)  # [[0, 2], [3, 4], [5, 6], [7, 8]]

nested_list[1] = [9, 10]  # Modifying the second sublist

print(nested_list)  # [[0, 2], [9, 10], [5, 6], [7, 8]]

nested_list.insert(2, [11, 12])  # Inserting a new sublist at index 2

print(nested_list)  # [[0, 2], [9, 10], [11, 12], [5, 6], [7, 8]]

nested_list.remove([11, 12])  # Removing the sublist at index 2

print(nested_list)  # [[0, 2], [9, 10], [5, 6], [7, 8]]
