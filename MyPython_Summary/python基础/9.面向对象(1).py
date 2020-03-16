class Document():
    def __init__(self, title, auther, context):
        print('init function called')
        self.title = title
        self.auther = auther
        self.__context = context  # __开头的是私有属性

    def get_context_length(self):
        return len(self.__context)

    def intercept_context(self, length):
        self.__context = self.__context[:length]

harry_potter_book = Document('Harry Potter', 'J. K. Rowling', '... Forever Do not believe any thing is capable of thinking independently ...')

print(harry_potter_book.title)
print(harry_potter_book.auther)
print(harry_potter_book.get_context_length())

print(harry_potter_book.__context)  # 这里运行会报错  因为私有属性不可见

# 类：一群有着相同属性和函数的对象的集合
# 两个问题
# 第一：然后和在一个类中定义一些常量，每个对象都可以方便访问这些常量而不用重新构造
# 第二：如果一个函数不涉及到访问修改这个类的属性，而放在类的外面不合适，怎样做才能更优雅

# Class Document2():
#     WELCOME_STR = 'welcome! The context for this book is{}'
#
#     def __init__(self, title, auther, context):
#         print('init function called')
#         self.title = title
#         self.auther = auther
#         self.__context = context
#
#     # 类函数
#     @classmethod
#     def create_empty_book(cls, title, author):
#         return cls(title = title, author = author, context = 'nothing')
#
#     # 成员函数
#     def get_context_length(self):
#         return len(self.__context)
#
#     # 静态函数
#     @staticmethod
#     def get_welcome(context):
#         return Document2.WELCOME_STR.format(context)

# 第一个问题：只需要和函数并列声明并赋值，就可以实现，在类中使用self.常量来使用，在类外使用Entity.常量 来使用
# 第二个问题：提出了类函数，成员函数，静态函数的概念，前两者是动态的，可以访问或修改对象的属性，而静态函数和类没有什么关系，最明显
# 的特征是，静态函数的第一个参数没有任何特殊性

# 继承是需要注意的是继承类生成对象时，是不会自动调用父类的构造函数的，因此必须在init()函数中显式的调用父类的构造函数，他们的执行顺序是：子类的构造函数 > 父类的构造函数



