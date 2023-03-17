"""
- 使用生成器函数得到生成器对象， 并反复的调用对象next() 方法实现数据的生成
- 函数中的yeild关键字的作用就是直接生成一个迭代器， 之后这个迭代器会调用next()
- 直到抛出stopIteration
- 使用生成器的好处
    - 数据是按需生成的，不用一次性在内存中创建大量空间
- 例子：
    - 生成300w个4位随机的验证码
"""
import random

def verify_code(num: int = 3000000, is_test: bool = False):
    assert isinstance(num, int), 'the type of num must be int...'
    if is_test:
        print(f'gengerate codes at once ...')
        code = [random.randint(1000, 9999) for _ in range(num)]
        idx = random.randint(0, num - 1)
        return code[idx]
    else:
        count = 0
        while count < num:
            code = random.randint(1000, 9999)
            yield code
            count += 1

if __name__ == "__main__":
    # print(verify_code(10).__next__())
    g = verify_code(10)
    # __iter__  __next__ 这些方法在生成器对象g中
    attr = dir(g)
    print(attr)
    for i in g:
        print(i)
