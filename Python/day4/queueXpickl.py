import pickle


class QueueOutOfRangeException(Exception):
    """Custom exception for when the queue size is full."""

    pass


class Queue:
    _instances = {}

    def __init__(self, name):
        self.__value = []
        self.name = name
        Queue._instances[name] = self

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
        return len(self.__value) == 0

    @classmethod
    def get_queue(cls, name):
        return cls._instances.get(name, None)

    @classmethod
    def save(cls, filename="queues.pkl"):

        with open(filename, "wb") as file:
            pickle.dump(cls._instances, file)
        print("Queues saved successfully.")

    @classmethod
    def load(cls, filename="queues.pkl"):
        try:
            with open(filename, "rb") as file:
                cls._instances = pickle.load(file)
                print("Queues loaded successfully.")
        except (FileNotFoundError, EOFError):
            print("No saved queues found.")


class QueuePlus(Queue):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    def insert(self, valuePlus):
        if len(self.value) >= self.size:
            raise QueueOutOfRangeException(f"Queue '{self.name}' is full.")

        self.value = valuePlus


# Example Usage
q1 = QueuePlus("Queue1", 3)
q2 = QueuePlus("Queue2", 2)

q1.insert(10)
q1.insert(20)

q2.insert(100)

retrieved_q1 = Queue.get_queue("Queue1")
print("Retrieved Queue1:", retrieved_q1.value)

Queue.save()

Queue.load()

retrieved_q2 = Queue.get_queue("Queue2")
print("Retrieved Queue2:", retrieved_q2.value)
