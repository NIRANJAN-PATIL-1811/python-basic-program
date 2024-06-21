class Example:
    data = 10
    
    def __init__(self, name):
        self.name = name
    
    def display(self):
        print("Name:", self.name)


# Displaying the namespace of the Example class
print("Namespace of Example class:")
print(Example.__dict__)