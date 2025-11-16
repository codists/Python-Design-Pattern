# @Filename: singleton_pattern_with_decorator.py
# @Author: codists
# @Created: 2025-11-16 17:24:57

def singleton(cls):
    # 有些写法这里用 instance = {} 也可以
    instance = None

    def wrapper(*args, **kwargs):
        nonlocal instance
        if instance is None:
            instance = cls(*args, **kwargs)
        return instance

    return wrapper

@singleton
class Singleton():
    def __init__(self, name):
        self.name= name

if __name__ == '__main__':
    # 输出: 初始化实例，名称: 第一个实例
    singleton1 = Singleton('第一个实例')
    # 输出: 初始化实例，名称: 第二个实例
    singleton2 = Singleton('第二个实例')

    # 输出: True
    # 虽然第二次名字变了，但 singleton1 和 singleton2 是同一个对象，即只有一个实例对象(单例模式保证的是实例数量)
    print(singleton1 is singleton2)  # True
