class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        # If no instance exists, create one and store it
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        # Return the existing instance
        return cls._instances[cls]

# Example usage
class SingletonClass(metaclass=SingletonMeta):
    def __init__(self, name):
        self.name = name

# Creating instances
instance1 = SingletonClass("Instance 1")
instance2 = SingletonClass("Instance 2")

# Both instances are the same
print(instance1 is instance2)  # Output: True

print(instance1.name)  # Output: Instance 1
print(instance2.name)  # Output: Instance 1
