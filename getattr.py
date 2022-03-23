class Foo:
    def __getattr__(self, attr):
        print("你调用了%s" % attr)
        return self.other

    def other(self, p1, p2):
        print(f'另外的函数,参数为{p1},{p2}')


f = Foo()
print('hello')
f.bar(1, 2)
'''
你调用了bar
另外的函数,参数为1,2
'''
