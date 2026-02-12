# WAP to demonstrate OOPs in Python using classes and objects

# OOP concept: Class -> a blueprint for objects
class Op1:
    # OOP concept: Class attributes (shared by all instances)
    a = 25  # class attribute
    b = 65  # class attribute

    # OOP concept: Constructor (__init__) - creates and initializes an object
    def __init__(self, val=None):
        # OOP concept: Instance attribute (unique to each object)
        self.instance_val = val


# OOP concept: Object / Instance -> a concrete occurrence of a class
objsamir = Op1()

# Accessing a class attribute via the class name
print(Op1.a)           # prints 25 (class attribute)

# Accessing attribute via an instance. If not found on instance,
# Python falls back to the class attribute with the same name
print(objsamir.b)      # prints 65 (class attribute accessed through instance)

# Modifying a class attribute (affects class-level value)
Op1.a = 96
print(Op1.a)           # prints 96 (modified class attribute)

# Notes (terms):
# - Class: `Op1`
# - Object/Instance: `objsamir`
# - Class attribute: `a`, `b`
# - Instance attribute: `instance_val` (set in constructor)
# - Constructor: `__init__`
# - Encapsulation: attributes grouped inside the class
# - Inheritance/Polymorphism/Abstraction: not shown here (would require
#   subclasses, method overriding, or hiding implementation details)


# --- Demonstration: instance variables vs class attributes ---
# Create an object with an instance value
o1 = Op1(10)
print(o1.instance_val)   # prints 10 -> this is an instance variable on o1

# Accessing class attribute through instance (falls back to class if
# instance has no such attribute)
print(o1.a)              # prints current class `a` value (96 from above)

# Shadowing the class attribute by assigning to the instance
o1.a = 200              # creates an instance attribute `a` on o1, shadows class's `a`
print(o1.a)              # prints 200 -> instance attribute
print(Op1.a)             # prints 96  -> class attribute unchanged

# A new object without its own `a` still reads the class attribute
o2 = Op1(20)
print(o2.a)              # prints 96 (reads class attribute)