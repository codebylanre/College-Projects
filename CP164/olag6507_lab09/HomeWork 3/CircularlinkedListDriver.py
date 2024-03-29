from CircularLinkedlist import CircularLinkedList




circlinked = CircularLinkedList()

# Add nodes

for i in ("ABC"):
    circlinked.add(i)


# Transverse and display
print('CircularLinkedList')
circlinked.transverse()


circlinked.remove('B')

print()
print("Circular linked list after edit")
circlinked.transverse()