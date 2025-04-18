import pickle


class QueueOutOfRangeException(Exception):
    """Custom EXCEPTION FOR WHEN QUEUE SIIZE IS FULL"""

    pass


class Queue:

    def __init__(self):
        self.__value = []

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value.append(value)
        print(self.__value)

    def Pop(self):
        if self.__value:
            return self.__value.pop(0)
        raise ValueError("Empty queue")

    def isEmpty(self):
        if self.__value == 0:
            return True


class QueuePlus(Queue):
    def __init__(self, name, size):
        super().__init__()
        self.name = name
        self.size = size

    def insert(self, valuePlus):

        if len(self.value) > self.size:
            raise QueueOutOfRangeException(f"Queue {self.name} is full.")
        try:
            self.value = valuePlus

        except Exception as e:
            print(e)


q1 = QueuePlus("FirstQueue", 3)
q2 = QueuePlus("SecondQueue", 2)

q1.insert(10)
q1.insert(230)
q1.insert(23)
q1.insert(90)
q1.insert(100)
q2.insert(20)
print(q1.value)
