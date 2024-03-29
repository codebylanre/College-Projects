from BinarySearchTree import BinarySearchTree




# Example usage:

# Using binary tree from class pdf so the key makes it intersting
bst = BinarySearchTree()
bst.insert(60, "Abdulbasit")
bst.insert(12, "Lanre")
bst.insert(90, "Codebylanre")
bst.insert(71, "iamabdulbasit")
bst.insert(100, "Gwen")
bst.insert(84, "Stacey")
bst.insert(4, "Jane")
bst.insert(41, "Fred")
bst.insert(1, "AB")
bst.insert(29, "Abdul")
bst.insert(23, "Basit")
bst.insert(37, "Lanre")

bst.print()

print()
smallest_data, smallest_key = bst.getSmallest_Iteration()
print(f"Smallest node Iteration: \nKey: {smallest_key}, Data: {smallest_data}")

print()
largest_data, largest_key = bst.getLargest_Iteration()
print(f"Largest node Iteration: \nKey: {largest_key}, Data: {largest_data}")

print()
smallest_data, smallest_key = bst.getSmallest_Recursive()
print(f"Smallest node Recursive: \nKey: {smallest_key}, Data: {smallest_data}")



print()
largest_data, largest_key = bst.getLargest_Recursive()
print(f"Largest node Recursive: \nKey: {largest_key}, Data: {largest_data}")


print()
data, level = bst.search(71)
print("Search")
print(f"Data: {data}, Level: {level}")


print()
print("Ancestor (First - Root)")
result = bst.Ancestors(23)
