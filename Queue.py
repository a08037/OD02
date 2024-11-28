class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Очередь пуста"

    def size(self):
        return len(self.items)

# Пример использования очереди
queue = Queue()
queue.enqueue("Документ 1")
queue.enqueue("Документ 2")
queue.enqueue("Документ 3")
print(queue.dequeue())  # Удаляет и возвращает "Документ 1"
print(queue.size())  # 2
