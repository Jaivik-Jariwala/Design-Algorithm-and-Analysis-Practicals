import time

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        self.length = 0
        
        if values is not None:
            for value in values:
                self.append(value)

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(value)

    def to_list(self):
        current = self.head
        values = []
        while current is not None:
            values.append(current.value)
            current = current.next
        return values

def add_lists(list1, list2):
    start_time = time.time()

    def _add(p1, p2, carry):
        if p1 is None and p2 is None:
            if carry:
                return LinkedList([carry])
            else:
                return LinkedList()

        if p1 is None:
            p1_value = 0
        else:
            p1_value = p1.value
            p1 = p1.next

        if p2 is None:
            p2_value = 0
        else:
            p2_value = p2.value
            p2 = p2.next

        carry, value = divmod(p1_value + p2_value + carry, 10)
        result = LinkedList([value])
        result.next = _add(p1, p2, carry)
        return result

    result = _add(list1.head, list2.head, 0)

    end_time = time.time()
    print("Running time:", end_time - start_time, "seconds")

    return result

def sub_lists(list1, list2):
    start_time = time.time()

    def _sub(p1, p2, borrow=0):
        if p1 is None and p2 is None:
            return LinkedList()

        if p1 is None:
            p1_value = 0
        else:
            p1_value = p1.value
            p1 = p1.next

        if p2 is None:
            p2_value = 0
        else:
            p2_value = p2.value
            p2 = p2.next

        diff = p1_value - p2_value - borrow
        if diff < 0:
            borrow = 1
            diff += 10
        else:
            borrow = 0

        result = LinkedList([diff])
        result.next = _sub(p1, p2, borrow)
        return result

    result = _sub(list1.head, list2.head)

    end_time = time.time()
    print("Running time:", end_time - start_time, "seconds")

    return result


def multiply_lists(list1, list2):
    start_time = time.time()

    def _multiply(p1, p2, carry):
        if p1 is None:
            return LinkedList()

        value = p1.value * p2.value + carry
        carry, value = divmod(value, 10)

        result = LinkedList([value])
        temp = _multiply(p1.next, p2, carry)

        if temp.head is None:
            return result
        else:
            current = temp.head
            while current.next is not None:
                current = current.next
            current.next = LinkedList([0])
            result = add_lists(result, temp)

        return result

    result = LinkedList()
    p2 = list2.head

    while p2 is not None:
        temp = _multiply(list1.head, p2, 0)

        if temp.head is None:
            result.append(0)
        else:
            result = add_lists(result, temp)

        p2 = p2.next

    end_time = time.time()
    print("Running time:", end_time - start_time, "seconds")

    return result

def power_lists(number, exponent):
    start_time = time.time()

    def _power(base, exp):
        if exp == 0:
            return LinkedList([1])

        temp = _power(base, exp // 2)
        if exp % 2 == 0:
            return multiply_lists(temp, temp)
        else:
            return multiply_lists(base, multiply_lists(temp, temp))
        
    end_time = time.time()
    print("Running Time: ", end_time - start_time, "seconds")

    return _power(number, int(''.join(map(str, exponent.to_list()))))



def create_linked_list():
    nums = input("Enter a list of integers separated by spaces: ").split()
    linked_list = LinkedList()
    for num in nums:
        linked_list.append(int(num))
    return linked_list

print("Select an operation to perform:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Power")
operation = int(input("Enter the number of the operation: "))

if operation == 1:
    list1 = create_linked_list()
    list2 = create_linked_list()
    result = add_lists(list1, list2)
elif operation == 2:
    list1 = create_linked_list()
    list2 = create_linked_list()
    result = sub_lists(list1, list2)
elif operation == 3:
    list1 = create_linked_list()
    list2 = create_linked_list()
    result = multiply_lists(list1, list2)
elif operation == 4:
    number = create_linked_list()
    exponent = create_linked_list()
    result = power_lists(number, exponent)
else:
    print("Invalid operation")
    exit()

print("Result: ", result.to_list())
