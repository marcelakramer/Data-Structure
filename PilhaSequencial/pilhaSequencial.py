class PilhaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class Pilha:
    def __init__(self):
        self.__items = list()


    def __str__(self) -> str:
        string = ''
        for i in range((len(self.__items)-1), -1, -1):
            string += f'{self.__items[i]}\n' 
        return string


    def __len__(self) -> int:
        return len(self.__items)

    
    def stackEmpty(self) -> bool:
        if (len(self.__items) == 0):
            return True

    
    def push(self, item:any):
        self.__items.append(item)


    def pop(self) -> any:
        if not self.stackEmpty():
            return self.__items.pop()
        else:
            raise PilhaException('The stack is empty.')

    def search(self, item:any) -> int:
        if not self.stackEmpty():
            for i in range(len(self.__items)):
                if self.__items[i] == item:
                    return i + 1
            else:
                raise PilhaException('This element is not in the stack.')
        else:
            raise PilhaException('The stack is empty.')


    def item(self, position:int) -> int:
        if not self.stackEmpty():
            try:
                return self.__items[position-1]
            except IndexError:
                raise PilhaException('Invalid position.')
        else:
            raise PilhaException('The stack is empty.')


    def modify(self, position:int, item:any):
        if not self.stackEmpty():
            try:
                self.__items[position-1] = item
            except IndexError:
                raise PilhaException('Invalid position.')
        else:
            raise PilhaException('The stack is empty.')


    def empty(self):
        self.__items.clear()

            
