class FilaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
    

class Fila:
    def __init__(self, length):
        self.items = [None for i in range(length)]
        self.start = 0
        self.end = -1
        self.length = length
        self.filled = 0


    def __str__(self) -> str:
        string = ''
        cursor = self.start
        while cursor <= self.end:
            string += f'{self.items[cursor]} '
            cursor = (cursor + 1) % self.length

        return string

    
    def lineEmpty(self) -> bool:
        return (self.filled == 0)

    
    def lineFull(self) -> bool:
        return (self.filled == self.length)

    
    def __len__(self) -> int:
        return self.filled

    
    def push(self, content:any):
        if self.lineFull():
            raise FilaException('The line is full.')
        
        self.end = (self.end + 1) % self.length
        self.items[self.end] = content
        self.filled += 1

    
    def pop(self) -> any:
        if self.lineEmpty():
            raise FilaException('The line is empty.')

        popContent = self.items[self.start] 
        self.start = (self.start + 1) % self.length
        self.filled -= 1

        return popContent


    def search(self, content:any) -> int:
        if self.lineEmpty():
            raise FilaException('The line is empty.')

        cursor = self.start
        count = 0
        for i in range(self.length):
            count += 1
            if self.items[cursor] == content:
                return count
            
            cursor = (cursor + 1) % self.length

        raise FilaException('This element is not in the line.')


    def item(self, position:int) -> any:
        if self.lineEmpty():
            raise FilaException('The line is empty.')

        try:
            assert position > 0 and position <= self.filled

            cursor = self.start
            count = 1

            while (count != position):
                count += 1
                cursor = (cursor + 1) % self.length

            return self.items[cursor]

        except AssertionError:
            raise FilaException('Invalid position.')


    def modify(self, position:int, content:any):
        if self.lineEmpty():
            raise FilaException('The line is empty.')

        try:
            assert position > 0 and position <= self.filled

            cursor = self.start
            count = 1

            while (count != position):
                count += 1
                cursor = (cursor + 1) % self.length

            self.items[cursor] = content

        except AssertionError:
            raise FilaException('Invalid position.')


    def empty(self):
        while not self.lineEmpty():
            self.pop()

    

        
