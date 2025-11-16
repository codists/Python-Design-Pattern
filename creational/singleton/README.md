# Python 知识点

下面介绍一些 Python 知识点，实现单例模式的时候会用到这些知识点。

## `__call__(self[, args...])`

根据 Python 官方文档的语言参考手册(Language reference，https://docs.python.org/3/reference/datamodel.html#object.__call__)：

> - object.**__call__**(*self*[, *args...*])
>
>   Called when the instance is “called” as a function; if this method is defined, `x(arg1, arg2, ...)` roughly translates to `type(x).__call__(x, arg1, ...)`. The [`object`](https://docs.python.org/3/library/functions.html#object) class itself does not provide this method.

上面的引用翻译成中文意思是：当实例(instance)像函数一样被“调用”时，`__call__() `方法会被调用。如果在一个类里面定义了`__call__() `方法，那么执行 `x(arg1, arg2, ...)`(注：x 在这里表示实例) 时实际执行的是`type(x).__call__(x, arg1, ...)`。`object`（所有类的基类）没有定义 `__call__()` 方法。

**注：**

1.类(如：User)为什么可以像函数 user = User() 一样调用呢？因为默认情况下，每个类都是元类(metaclass) type 的实例，type 里面定义了 `__call__()` 方法。

```
class User:
    def __init__(self, name):
        self.name = name

print(type(User))  # <class 'type'>
```

2.元类 type 是最顶层的元类，那 type 为什么可以像函数 type() 一样调用呢？因为它的元类就是它自己，调用的是自己的`__call__() `方法，即“自举(bootstrapping)”。

```
print(type(type)) # <class 'type'>, type 的元类是 type
```

## `__new__(cls[, ...])` 

根据 Python 官方文档的语言参考手册(Language reference，https://docs.python.org/3/reference/datamodel.html#object.__new__)：

> Called to create a new instance of class *cls*...

上面的引用翻译成中文意思是：可以调用 `__new__()`  创建 *cls* 类的实例。

## `__init__(self[, ...])`

根据 Python 官方文档的语言参考手册(Language reference，https://docs.python.org/3/reference/datamodel.html#object.__init__：

> Called after the instance has been created (by [`__new__()`](https://docs.python.org/3/reference/datamodel.html#object.__new__)), but before it is returned to the caller. ..

上面的引用翻译成中文意思是：`__init__()`方法在实例 (通过 [`__new__()`](https://docs.python.org/zh-cn/3.14/reference/datamodel.html#object.__new__)) 被创建之后，返回给调用者之前调用。

# singleton pattern(单例模式)

## 定义(what)

根据维基百科(https://en.wikipedia.org/wiki/Singleton_pattern)：

> In object-oriented programming, the singleton pattern is a software design pattern that restricts the instantiation of a class to a singular instance(在面向对象编程中，**单例模式是一种**限制类只有一个实例的**设计模式**)。

## 目的(why)

TBD

## 示例

1. 使用`__new__()`实现

   详见: [./singleton_pattern_with_new_method.py](singleton_pattern_with_new_method.py)

2. 使用装饰器实现(函数装饰器/类装饰器)实现

   详见: [./singleton_pattern_with_decorator.py](singleton_pattern_with_decorator.py)

3. 使用 metaclass(元类) 实现

   详见: [./singleton_pattern_with_metaclass.py](singleton_pattern_with_metaclass.py)

# 说明

1.很遗憾，因本人水平有限，这些 demo 的写法都没有在实际的 Python library 或者 framework 中找到，待后续找到再补充。

