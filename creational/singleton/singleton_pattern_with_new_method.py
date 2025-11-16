# @Filename: singleton_pattern_with_new_method.py
# @Author: codists
# @Created: 2025-11-16 15:30:41

class Singleton:
    # 有些写法使用单下划线开头(_instance)表示这是"私有变量"，内部使用。
    # 有些写法用双下划线开头(__instance)，非常不好。因为双下划线开头的意思是"name mingling"，使用目的不匹配
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            # 为什么使用 super() 呢？为了让代码更通用，兼容有继承的情况。
            # 这里的 Singleton 显式继承其它类，直接用 object.__new__(cls) 也是一样的效果
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, name):
        self.name = name
        print(f"初始化实例，名称: {name}")

if __name__ == '__main__':
    # 输出: 初始化实例，名称: 第一个实例
    singleton1 = Singleton('第一个实例')
    # 输出: 初始化实例，名称: 第二个实例
    singleton2 = Singleton('第二个实例')

    # 输出: True
    # 虽然第二次名字变了，但 singleton1 和 singleton2 是同一个对象，即只有一个实例对象(单例模式保证的是实例数量)
    print(singleton1 is singleton2) # True