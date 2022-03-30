'''
timer() 是我们定义的装饰器函数，
使用@把它附加在任何一个函数（比如do_something）定义之前，
就等于把新定义的函数，当成了装饰器函数的输入参数。
运行 do_something() 函数，可以理解为执行了timer(do_something) 。
细节虽然复杂，不过这么理解不会偏差太大，且更易于把握装饰器的制造和使用。
'''

import time
def timer(func):
    def wrapper(*args,**kwds):
        t0 = time.time()
        func(*args,**kwds)
        t1 = time.time()
        print("耗时为%0.3f" % (t1-t0,))
    return wrapper

@timer
def do_something(delay):
    print('do something')
    time.sleep(delay)
    print('did something')
do_something(3)
