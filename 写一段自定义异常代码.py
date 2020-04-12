""""""
"""自定义异常用raise抛出异常"""
"""Exception函数可以被用来触发，或者定义一个子类集成Exception"""
try:
    for i in range(5):
        if i > 2:
            raise Exception('数字大于2')
except Exception as ret:
    print(ret)
