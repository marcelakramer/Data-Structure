class FilaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class HeadNode:
    def __init__(self):
        self.start = None
        self.end = None
        self.length = 0


class Node:
    def __init__(self, content:any):
        self.content = content
        self.next = None

    def __str__(self) -> str:
        return f'{self.content}'


class Fila:
    def __init__(self):
        self.head = HeadNode()


    def __str__(self) -> str:
        string = ''
        cursor = self.head.start
        while cursor:
            string += f'{cursor.content} '
            cursor = cursor.next

        return string

    
    def lineEmpty(self) -> bool:
        return self.head.length == 0 

    
    def __len__(self) -> int:
        return self.head.length

    
    def push(self, content):
        newNode = Node(content)

        if self.lineEmpty():
            self.head.start = newNode
            self.head.end = newNode    
        else:
            self.head.end.next = newNode
            self.head.end = newNode
        
        self.head.length += 1
    
    def pop(self) -> any:
        if self.lineEmpty():
            raise FilaException('The line is empty.')
        
        popContent = self.head.start.content
        self.head.start = self.head.start.next
        self.head.length -= 1

        return popContent

    
    def search(self, content:any) -> int:
        if self.lineEmpty():
            raise FilaException('The line is empty.')
        
        cursor = self.head.start
        count = 1
        while cursor:
            if cursor.content == content:
                return count

            cursor = cursor.next
            count += 1

        raise FilaException('This element is not in the line.')


    def item(self, position:int) -> any:
        if self.lineEmpty():
            raise FilaException('The line is empty.')

        try:
            assert position > 0 and position <= self.head.length

            cursor = self.head.start
            count = 1
            while count != position:
                cursor = cursor.next
                count += 1

            return cursor.content

        except AssertionError:
            raise FilaException('Invalid position.')

        
    def modify(self, position:int, content:any):
        if self.lineEmpty():
            raise FilaException('The line is empty.')

        try:
            assert position > 0 and position <= self.head.length

            cursor = self.head.start
            count = 1
            while count != position:
                cursor = cursor.next

            cursor.content = content

        except AssertionError:
            raise FilaException('Invalid position.')


    def empty(self):
        while not self.lineEmpty():
            self.pop()
            


