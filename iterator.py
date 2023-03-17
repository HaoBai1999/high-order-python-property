"""
- 迭代器本质上就是自己写一个类，并在类中实现 __iter__, __next__ 方法
- __iter__ 只会被调用一次， 但是__next__会被调用多次.
- 本质上讲， 生成器就是一个迭代器，yield 会自己实现__iter__ 方法
- 使用迭代器的好处
    - 数据是按需生成的，不用一次性在内存中创建大量空间
- 例子：
    - 生成300w个4位随机的验证码
"""

import random


class MyIter(object):
    def __init__(self, num: int = 3000000) -> None:
        super().__init__()
        self.num = num
        self.count = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count < self.num:
            self.count += 1
            return random.randint(1000, 9999)
        else:
            raise StopIteration

if __name__ == "__main__":
    my_iter = MyIter(10)
    # __iter__  __next__
    print(dir(my_iter))
    for i in my_iter:
        print(i)
