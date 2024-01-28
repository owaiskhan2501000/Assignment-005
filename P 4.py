class MultipleInheritanceMeta(type):
    def __new__(cls, name, bases, attrs):
        # Ensure that the class inherits from at least two specific parent classes
        required_parents = getattr(cls, 'required_parents', [])

        if len(bases) < len(required_parents):
            raise TypeError(f"{name} must inherit from at least {len(required_parents)} parent classes")

        return super().__new__(cls, name, bases, attrs)

# Example usage
class Parent1:
    pass

class Parent2:
    pass

class MyClass(Parent1, Parent2, metaclass=MultipleInheritanceMeta):
    pass

# This will raise a TypeError because MyClass does not inherit from at least two parent classes
