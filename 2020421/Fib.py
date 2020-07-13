class FibIterator:


# 补全这个迭代器的代码，实现要求的功能
    def __init__(self,num):
        self.a=1
        self.b=1
        self.num= num
        self.count=0

        for i in range(num-1):
            self.a = self.b
            self.b = self.a+self.b
        return self.a
    def __iter__(self):
        return self
    def __next__(self):
        value=self.a
        self.a = self.b
        self.b = self.a + self.b
        self.count += 1
        if self.count>self.num:
            raise StopIteration
        return value





def GetFib(count):
    # 在此处返回一个FibIterator的对象
    return FibIterator

for i in range(9):
    print(GetFib(9).next)






    class FibIterator:
        count = 0
        now = 1 #初始值分别设置为1和0，方便__next__函数处理
        last = 0 #
        def __init__(self,count):
            self.count = count
        def __iter__(self):
            return self
        def __next__(self):
            if self.count == 0:
                raise StopIteration
            ret = self.now
            t = self.now
            self.now = self.last + self.now #在数列中前进一个数字
            self.last = t
            self.count -= 1
            return ret
    def GetFib(count):
        return FibIterator(count)



    def myrange(start,stop,step):
        if step > 0:
            while start < stop:
                yield start
                start += step
        elif step < 0:
            while start > stop:
                yield start
                start += step
        else:
            while True:
                yield start

