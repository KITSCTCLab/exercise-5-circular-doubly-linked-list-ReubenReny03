class Node:
    def __init__(self, data=None):
        self.data = data
        self.previous = self
        self.next = self


class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def add_at_tail(self, data) -> bool:
        if self.head is None:
            new_node = Node(data)
            new_node.next = new_node
            new_node.previous = new_node
            self.head = new_node
            count +=1
            return True
        else:
            new_node = Node(data)
            new_node.next = self.head
            prep = self.head
            for x in range(count-1):
                prep = prep.next
            prep.next = new_node
            new_node.previous = prep
            count +=1
            return True

    def add_at_head(self, data) -> bool:
        if self.head is None:
            new_node = Node(data)
            new_node.next = new_node
            new_node.previous = new_node
            self.head = new_node
            count +=1
            return True
        else:
            new_node = Node(data)
            new_node.next = self.head
            prep = self.head
            new_node.previous = prep.previous
            prep.previous = new_node
            count +=1
            return True

    def add_at_index(self, index, data) -> bool:
        if (index >= count) or (index < 0 ):
            return False
        if self.head is None:
            new_node = Node(data)
            new_node.next = new_node
            new_node.previous = new_node
            self.head = new_node
            count +=1
            return True
        else:
            
            if (index == 0):
                temp = self.head
                new_node = Node(data)
                new_node.next = temp
                temp.previous = temp
                for x in range(count - 1):
                    temp.next
                temp.next = new_node
                new_node.previous = temp
                count +=1
                self.head = new_node
                return True
            else:
                temp = self.head
                for x in range (index):
                    temp = temp.next
                new_node = Node(data)
                repre = temp.previous
                temp.previous = new_node
                new_node.next = temp
                new_node.previous = repre
                repre.next = new_node
                count +=1
                return True
    def get(self, index) -> int:
        if (index >= self.count) or (index < 0):
            return -1
        if self.head is None:
            return None
        temp = self.head
        if index == 0:
            return temp.data
        else:
            for x in range (index):
                temp = temp.next
            return temp.data
        

    def delete_at_index(self, index) -> bool:
        if (index >= self.count) | (index < 0):
            return False
        if self.count == 1:
            self.head = None
            self.count -= 1
            return True

        target = self.head
        for x in range(index):
            target = target.next

        if target is self.head:
            self.head = self.head.next

        target.previous.next, target.next.previous = target.next, target.previous
        self.count -= 1

    def get_previous_next(self, index) -> list:
        if (index >= self.count) or (index < 0) or self.head is None:
            return [-1]
        else:
            if self.count == 1:
                return [self.head.previous.data, self.head.next.data]
            else:
                my_counter = 0
                temp = self.head
                while my_counter < index:
                    temp = temp.next
                    my_counter += 1
                return [temp.previous.data, temp.next.data]   


# Do not change the following code
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = []
iteration_count = 0

for item in input_data.split(', '):
    inner_list = []
    if item.isnumeric():
        data.append(int(item))
    elif item.startswith('['):
        item = item[1:-1]
        for letter in item.split(','):
            if letter.isnumeric():
                inner_list.append(int(letter))
        data.append(inner_list)

obj = DoublyCircularLinkedList()
result = []
for i in range(len(operations)):
    if operations[i] == "add_at_head":
        result.append(obj.add_at_head(data[i]))
    elif operations[i] == "add_at_tail":
        result.append(obj.add_at_tail(data[i]))
    elif operations[i] == "add_at_index":
        result.append(obj.add_at_index(int(data[i][0]), data[i][1]))
    elif operations[i] == "get":
        result.append(obj.get(data[i]))
    elif operations[i] == "get_previous_next":
        result.append(obj.get_previous_next(data[i]))
    elif operations[i] == 'delete_at_index':
        result.append(obj.delete_at_index(data[i]))

print(result)
