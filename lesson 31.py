# class A(object):
#
#     def __init__(self):
#         self.a = 5
#         self.b = 7
#
#     def get_multiply(self):
#         return self.a * self.b
#
# class B(object):
#
#     def __init__(self):
#         self.c = 2
#         self.d = 6
#
#     def get_sum(self):
#         return self.c + self.d
#
# class C(B, A):
#     def __init__(self):
#         A.__init__(self)
#         B.__init__(self)
#
#
# c = C()
# print(c.get_multiply())
# print(c.get_sum())
# +++++++++++++++++++++++++++++++++++++++
# class A():
#
#     def __init__(self):
#         self.a = 2
#         self.b = 6
#
#     def get_multiply(self):
#         return self.a * self.b
#
#
# class B(A):
#
#     def __init__(self):
#         A.__init__(self)
#         self.c = None
#
#     def get_multiply(self):
#         self.c = A.get_multiply(self)
#         return 'B' * self.c
#
#
# b = B()
# print(b.get_multiply())
# ***************************************

class User(object):

    def __init__(self, first_name: str = 'Dima', age: int = 32, city: str = 'Minsk') -> None:
        self.city = city
        self.age = age
        self.first_name = first_name

    def info(self) -> str:
        return f'{self.first_name}: {self.age} from {self.city}'

    @staticmethod
    def foo():
        print("I'm Static Method!")


User.foo()






















