class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Стек пуст"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Стек пуст"

    def size(self):
        return len(self.items)

# Пример использования стека
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.pop())  # Удаляет и возвращает последний добавленный элемент (30)
print(stack.peek())  # Возвращает 20 без удаления
print(stack.is_empty())  # False
