class LoggingMeta(type):
    def __new__(cls, name, bases, attrs):
        # Log class creation
        print(f"Creating class: {name}")
        return super().__new__(cls, name, bases, attrs)

    def __init__(cls, name, bases, attrs):
        # Log class initialization
        print(f"Initializing class: {name}")
        super().__init__(name, bases, attrs)


class MyClass(metaclass=LoggingMeta):
    def __init__(self):
        print("Initializing instance of MyClass")


# Example usage
obj = MyClass()
