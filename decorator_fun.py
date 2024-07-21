# class Decorator:
#     def first(self, fun):
#         def second():
#             print("first")
#             fun()
#             print("second")
#         return second

# x = Decorator()
# @x.first
# def myfun():
#     print("Hello World!")

# myfun()
class Decorator:
    def first(self, fun):
        def second():
            print("first")
            fun()
            print("second")
        return second

# Use the class instance directly as a decorator
@Decorator.first
def myfun():
    print("Hello World!")

# Call the decorated function
myfun()

