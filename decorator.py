"""
- 这里所谓的装饰器就是在调用函数之前对函数做一些操作，
- 同样的在函数返回的时候做一些额外的操作
- 用装饰器的好处
    - 被装饰的函数可以按照原先的函数名正常的调用和传入参数
"""
def out(method):
    """
    method: is a function name
    """
    def inner(param: int = 0):
        """
        param:
            这个装饰器只能接受一个参数
        """
        print(f'before method !!')
        if param == 0:
            res =  method()
        else:
            res = method(param)
        print(f'before method !!')
        return res
    return inner    

def out_mul(method):
    """
    method: is a function name
    """
    def inner(*args, **kwargs):
        """
        这个装饰器可以接受任意的参数，但是具体如何传入参数依赖于
        被装饰的函数
        """
        print(f'before method !!')
        res =  method(*args, **kwargs)
        print(f'before method !!')
        return res
    return inner    

@out
def func():
    print(f'i am in func')
    return 44

@out
def func_one_param(param: int):
    print(f'i am in func_one_param, with number is {param}')
    return 1

@out_mul
def func_params(param1, param2):
    print(f'i am in func_params, with number are {param1, param2}')
    return 2
    

# func = out(func)


# func_one_param = out(func_one_param)

# func_params = out_mul(func_params)


if __name__ == "__main__":
    # 没有参数的装饰器
    # print(func())

    # 带有参数的装饰器
    # print(func_one_param(88))

    # 可以接受任何参数的装饰器
    print(func_params(55, 66))
    # params = (11, 22)
    # print(func_params(*params))

