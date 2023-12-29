from Node import Node
from LinkedList import LinkedList

# 1. Write a function copy which takes a LinkedList and returns a new LinkedList object with
# the same values of data at each Node.

def copy(linked):
    new_ll = LinkedList()
    
    current = linked.head
    
    for index in range(linked.length()):
        new_ll.add(current.getData())
        current = current.getNext()
    
    return new_ll

# 2. Write a function is_sorted which takes a LinkedList and returns a boolean value for
# whether the LinkedList is sorted in ascending order.

def is_sorted(ll: LinkedList):
    original = []
    new = []

    new_ll = ll.mergeSort()

    current = ll.head
    current_new = new_ll.head

    for index in range(ll.length()):
        original.append(current.getData())
        current = current.getNext()

    for index in range(new_ll.length()):
        new.append(current_new.getData())
        current_new = current_new.getNext()

    return original == new

# 3. Write a function strictly_greater which takes two LinkedList objects, A and B, and
# returns true if for all i, the element at position i of LinkedList A is greater than the element of
# position i of LinkedList B, false otherwise.

def strictly_greater(ll_a:LinkedList, ll_b:LinkedList):
    sorted_a = ll_a.mergeSort()
    sorted_b = ll_b.mergeSort()

    if sorted_a[0] >  sorted_b[ll_b.length() - 1]:
        return True
    else:
        return False

# 4. Write a function max_at_each_position which takes two LinkedList objects, A and B,
# which returns a new LinkedList with the the greater value at position i of LinkedList A and
# B, If either LinkedList A or B has no value at position i, then the one that does have a value is
# the greater value.

def max_at_each_position(a : LinkedList, b : LinkedList):
    new_ll = LinkedList()

    current_a = a.head
    current_b = b.head
    counter = 0

    min_count = min(a.length(), b.length())

    while counter < min_count:
        if current_a.getData() > current_b.getData():
            new_ll.add(current_a.getData())
        else:
            new_ll.add(current_b.getData())

        current_a = current_a.getNext()
        current_b = current_b.getNext()
        counter += 1

    while (current_a is not None):
        new_ll.add(current_a.getData())
        current_a = current_a.getNext()
        counter +=1

    while (current_b is not None):
        new_ll.add(current_b.getData())
        current_b = current_b.getNext()

    return new_ll


# 5. Write a function remove_dupes which takes a sorted LinkedList in ascending order and
# returns a new LinkedList object with the duplicates removed.

def remove_dupes(sorted_list):
    pass

# 6. Write a function merge(LinkedListA, LinkedListB) which returns the merging of LinkedListA
# and LinkedListB, much like you did in lab 7 with built-in lists. Your code should have
# complexity no bigger than O(N).

def merge(A, B):
    pass

# 7. **challenge** Write a function repeated which takes two sorted LinkedLists, that
# produces LinkedList with all values that are present in both LinkedLists. In O(n) time. If
# value appears multiple times in both LinkedLists, it should only appear once in the
# returned LinkedList.

if __name__ == "__main__":
    ll = LinkedList()
    ll.add(3)
    ll.add(1)
    ll.add(2)

    # a_ll = copy(ll)
    # print(a_ll)

    # print(is_sorted(ll))

    ll_a = LinkedList()
    ll_b = LinkedList()
    ll_a.add(1)
    ll_a.add(5)
    ll_a.add(10)
    ll_a.add(23)
    ll_b.add(2)
    ll_b.add(50)
    ll_b.add(9)

    # print(strictly_greater(ll_a, ll_b))

    # max_position = max_at_each_position(ll_a, ll_b)
    # print(max_position) 