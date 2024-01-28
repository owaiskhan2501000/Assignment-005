class AttributeValidationMeta(type):
    def __new__(cls, name, bases, attrs):
        for attr_name, attr_value in attrs.items():
            if isinstance(attr_value, str):
                # Validate string attribute length
                min_length = getattr(cls, 'min_length', None)
                max_length = getattr(cls, 'max_length', None)

                if min_length is not None and len(attr_value) < min_length:
                    raise ValueError(f"{attr_name} is too short. Minimum length: {min_length}")
                
                if max_length is not None and len(attr_value) > max_length:
                    raise ValueError(f"{attr_name} is too long. Maximum length: {max_length}")

        return super().__new__(cls, name, bases, attrs)

# Example usage
class Person(metaclass=AttributeValidationMeta):
    name = "John Doe"
    age = 30

    min_length = 3
    max_length = 10

# This will raise a ValueError because "name" has length less than the specified minimum
