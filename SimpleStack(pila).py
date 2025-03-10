class Stack(object):
    def __init__(self, max):
        self.__stackList = [None] * max
        self.__top = -1

    def push1(self, item):
        if self.isFull():
            raise IndexError("Stack is full")
        self.__top += 1
        self.__stackList[self.__top] = item


    def push2(self, item):
        if self.isFull():
            raise IndexError("Stack is full")
        
        userWord = input("Introduzca la palabra ")  # No es necesario usar str()
        userword = userWord[::-1]
        
        for char in userWord:  # Iterar sobre todos los caracteres
            self.push1(char)   # Llamar correctamente a push1()

        


    def pop(self):
        if self.isEmpty():
            raise IndexError("Stack is empty")
        top = self.__stackList[self.__top]
        self.__stackList[self.__top] = None
        self.__top -= 1
        return top

    def isEmpty(self):
        return self.__top < 0

    def isFull(self):
        return self.__top >= len(self.__stackList) - 1

    def __len__(self):
        return self.__top + 1

    def __str__(self):
        ans = "["
        for i in range(self.__top + 1):  # Corrección aquí para incluir el último elemento
            if len(ans) > 1:
                ans += ", "
            ans += str(self.__stackList[i])
        ans += "]"
        return ans

    def peek(self):
        if not self.isEmpty():
            return self.__stackList[self.__top]


stack = Stack(100)

stack.push2("hola")
print(stack)

expr = input("Expresion to check: ")
errors = 0

for pos, letter in enumerate(expr):
    if letter in "{([":
        if stack.isFull():
            raise Exception("Stack overflow on expression")
        
        else:
            stack.push1(letter)
    
    elif letter in "})]":
        if stack.isEmpty():
            print("Error: ", letter, "at position", pos, "has no matching left delimeter")
        
        errors += 1
        else:
            left = stack.pop()
