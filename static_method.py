class Static_method:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def stat(name: str, args: tuple) -> str:
        if not isinstance(name, int) or not isinstance(args, tuple):
            raise TypeError("Name must be an integer.")
            # print("sorry")
        # return f"{name} {args}"
        

if __name__ == "__main__":
    result = Static_method("roshan", 23)
    x = result.stat('neer', (5,2,4,5,3))
    # print(x)


# class StaticMethod:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @staticmethod
#     def stat(name: int, args: tuple) -> str:
#         if not isinstance(name, int):
#             raise TypeError("Name must be an integer.")
#         return f"{name} {args}"

# if __name__ == "__main__":
#     result = StaticMethod("roshan", 23)
#     print(result.stat('neer', (5, 2, 4, 5, 3)))  # Raises TypeError
