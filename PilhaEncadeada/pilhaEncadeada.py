class PilhaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class Node():
    def __init__(self, content:any):
        self.__content = content
        self.__next = None

    def __str__(self):
        return str(self.__content)

    @property
    def content(self) -> any:
        return self.__content

    @property
    def next(self):
        return self.__next

    @content.setter
    def content(self, newContent):
        self.__content = newContent

    @next.setter
    def next(self, newNext):
        self.__next = newNext


class Pilha:
    def __init__(self):
        self.__head = None
        self.__length = 0

    @property
    def head(self) -> Node:
        return self.__head
    
    def __str__(self) -> str:
        string = ''
        cursor = self.__head
        while (cursor):
            string += f'{cursor}\n'
            cursor = cursor.next

        return string


    def __len__(self) -> int:
        return self.__length

    
    def stackEmpty(self) -> bool:
        return self.__head == None

    
    def push(self, content:any):
        newNode = Node(content)
        newNode.next = self.__head
        self.__head = newNode
        self.__length += 1

    
    def pop(self) -> any:
        if self.stackEmpty():
            raise PilhaException('The stack is empty.')
        popContent = self.__head.content
        self.__head = self.__head.next
        self.__length -= 1
        return popContent

    def popN(self, times:int) -> bool:
        if self.stackEmpty():
            raise PilhaException('The stack is empty.')

        cursor = self.__head
        count = 0
        while count < times:
            try:
                self.pop()
                cursor = cursor.next
                count += 1

            except:
               return False
        
        return True

    
    def underHead(self) -> any:
        if self.stackEmpty():
            raise PilhaException('The stack is empty.')

        if self.__length == 1:
            raise PilhaException('The stack has no underHead.')

        underHeadNode = self.__head.next
        return underHeadNode.content

    
    def stackBase(self) -> any:
        if self.stackEmpty():
            raise PilhaException('The stack has no base.')
        
    
        cursor = self.__head
        count = 1
        while count != self.__length:
            cursor = cursor.next
            count += 1
            
        return cursor.content
       

    
    def search(self, content:any) -> int:
        if self.stackEmpty():
            raise PilhaException('The stack is empty.')
        else:
            cursor = self.__head
            count = 0
            while cursor:
                if cursor.content == content:
                    return self.__length - count
                
                count += 1
                cursor = cursor.next

            raise PilhaException('This item is not in the stack.')


    def item(self, position:int) -> any:
        if self.stackEmpty():
            raise PilhaException('The stack is empty.')
        else:
            try:
                assert position > 0 and position <= self.__length
                cursor = self.__head
                count = self.__length
                while count != position:
                    cursor = cursor.next
                    count -= 1
                return cursor.content

            except AssertionError:
                raise PilhaException('Invalid position.')


    def modify(self, position:int, content:any):
        if self.stackEmpty():
            raise PilhaException('The stack is empty.')
        else:
            try:
                assert position > 0 and position <= self.__length
                cursor = self.__head
                count = self.__length
                while count != position:
                    cursor = cursor.next
                    count -= 1

                cursor.content = content

            except AssertionError:
                raise PilhaException('Invalid position.')


    def empty(self):
        if self.stackEmpty():
            raise PilhaException('The stack is already empty.')
        else:
            while not self.stackEmpty():
                self.pop()


        
