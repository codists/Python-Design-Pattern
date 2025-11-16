# @Filename: singleton_pattern_with_metaclass.py
# @Author: codists
# @Created: 2025-11-16 18:45:40

class SingletonMeta(type):

    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, "instance"):
            cls.instance = super().__call__(*args, **kwargs)
        return cls.instance

class Singleton(metaclass=SingletonMeta):
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    # 输出: 初始化实例，名称: 第一个实例
    singleton1 = Singleton('第一个实例')
    # 输出: 初始化实例，名称: 第二个实例
    singleton2 = Singleton('第二个实例')

    # 输出: True
    # 虽然第二次名字变了，但 singleton1 和 singleton2 是同一个对象，即只有一个实例对象(单例模式保证的是实例数量)
    print(singleton1 is singleton2)  # True
