# main.py
from single_linked_list import SingleLinkedList

if __name__ == "__main__":
    data_list = [1, 3, 4, 5, 6, 8, 7, 9, 2, 22, 15, 55, 45, 23, 24, 26, 28]
    sll = SingleLinkedList()

    # Insert elements from the list into the linked list
    for data in data_list:
        sll.insert(data)

    # Display the linked list
    sll.display()
