from OOP.task_3_Array.TArray import TArray

array = TArray(num=5, data=[19, 2, 1, 3, 7, 0])
print(array.sorted())

print(array.min())
print(array.max())
print(array.fill_index(3, 0))
print(array.min())
print(array * 4)

array2 = TArray(array_to_copy=array)
print(array2)
