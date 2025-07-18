# 概述

工厂模式是 factory method pattern(工厂方法模式) 和 abstract factory pattern(抽象工厂模式)的统称。 

虽然有些文章会将 simple factory 也称为设计模式，但在《设计模式》这本书里面没有并没有提到 simple factory。在《Head First Design Patterns》提到："The Simple Factory isn’t actually a Design Pattern; it’s more of a programming idiom. But it is commonly used, so we’ll give it a Head First Pattern Honorable Mention. Some developers do mistake this idiom for the Factory Pattern, but the next time that happens you can subtly show you know your stuff; just don’t strut as you educate them on the distinction.(其实，简单工厂(Simple Factory)并不是一种设计模式；它更像是一种编程惯用法(idiom))，但由于这种惯用法被广泛使用，所以我们在《Head First 设计模式》这本书中给予它一个荣誉提名。一些开发者误以为这种惯用法就是工厂模式，下次遇到这种情况时，你可以巧妙地展示自己的专业见解。只是，当你告诉他们两者区别的时候别太趾高气扬)。所以本文章将 simple factory 当做一种 idiom，而不是一种 design pattern。

# simple factory idiom(简单工厂惯用法)

- 说明

1.仅有一个工厂类负责所有对象的创建。

2.通过参数决定创建哪种对象。

3.不符合开闭原则（新增类别需修改工厂类代码）。

4.返回的是具体实现(不是抽象类)。

- 好处

  

- 示例

[./1_simple_factory_idiom.py](1_simple_factory_idiom.py)

# factory method(工厂方法模式)

- 说明
- 好处
- 示例

# abstract method(抽象工厂模式) 

- 说明

1.抽象工厂包含多个工厂方法。

- 好处



- 示例
- 现实例子

1.factory_boy: https://github.com/FactoryBoy/factory_boy

2.model_bakery: https://github.com/model-bakers/model_bakery

# 总结

1.client 与 factory 的思想。