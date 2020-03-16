from abc import ABCMeta, abstractmethod


class Entity(metaclass=ABCMeta):
    @abstractmethod
    def get_title(self):
        pass

    @abstractmethod
    def set_title(self, title):
        pass


class Document(Entity):
    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

document = Document()
document.set_title('Harry Potter')
print(document.get_title())

entity = Entity()  # 这里直接运行会报错，只有通过Document继承Entity才能正常使用，因为直接只用entity对象是没有意义的
