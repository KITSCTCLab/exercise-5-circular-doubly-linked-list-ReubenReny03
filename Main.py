class Node:
    '''
    The Class Node just has 1 initilization function
    this class is used to make a Node
    '''
    def __init__(self, data=None):
        '''
        instance in the class
        
        data --> to store data
        previous --> to store location of previous data
        next --> to store location of next data
        '''
        self.data = data
        self.previous = self
        self.next = self


class DoublyCircularLinkedList:
    '''
    its a class to control the linked list
    '''
    def __init__(self):
        '''
        it has 2 instance
        head --> to point at the first element
        count --> to keep a count of node
        '''
        self.head = None
        self.count = 0

    def add_at_tail(self, data) -> bool:
        '''
        to add a node at the end of the linked list
        '''
        if self.head is None:
            '''
            if there is no node
            '''
            new_node = Node(data)
            new_node.next = new_node
            new_node.previous = new_node
            self.head = new_node
            self.count +=1
            return True
        else:
            '''
            if nodes are present
            '''
            new_node = Node(data)
            new_node.next = self.head
            prep = self.head
            for x in range(self.count-1):
                prep = prep.next
            prep.next = new_node
            new_node.previous = prep
            self.count +=1
            return True

    def add_at_head(self, data) -> bool:
        '''
        to add a node to the head or start
        '''
        if self.head is None:
            # if there is no node
            new_node = Node(data)
            new_node.next = new_node
            new_node.previous = new_node
            self.head = new_node
            self.count +=1
            return True
        else:
            # if node pre exist
            new_node = Node(data)
            new_node.next = self.head
            prep = self.head
            new_node.previous = prep.previous
            prep.previous = new_node
            self.count +=1
            return True

    def add_at_index(self, index, data) -> bool:
        '''
        to add a node at a perticular index
        '''
        if (index >= self.count) or (index < 0 ):
            # if invalid index number
            return False
        if self.head is None:
            # if list is empty
            new_node = Node(data)
            new_node.next = new_node
            new_node.previous = new_node
            self.head = new_node
            self.count +=1
            return True
        else:
            # if list is not empty
            if (index == 0):
                # if the given index was 0
                temp = self.head
                new_node = Node(data)
                new_node.next = temp
                temp.previous = temp
                for x in range(self.count - 1):
                    temp.next
                temp.next = new_node
                new_node.previous = temp
                self.count +=1
                self.head = new_node
                return True
            else:
                # other conditions
                temp = self.head
                for x in range (index):
                    temp = temp.next
                new_node = Node(data)
                repre = temp.previous
                temp.previous = new_node
                new_node.next = temp
                new_node.previous = repre
                repre.next = new_node
                self.count +=1
                return True
    def get(self, index) -> int:
        #get the data of a node at a perticular index
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
        # delete the node at a perticular index
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
        return True

    def get_previous_next(self, index) -> list:
        # get the data of previous and next node
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
