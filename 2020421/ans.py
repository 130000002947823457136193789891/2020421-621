class Vector3d:
    # 请在这里补充代码，完成本关任务
    #********** Begin *********#
    def __init__(self,x,y,z):
        self.__x=x
        self.__y=y
        self.__z=z
    #********** End *********#



import math as m
class Vector3d:
    def __init__(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z

    def length(self):
        # 请在这里补充代码，完成本关任务
        #********** Begin *********#
        ans=m.sqrt(self.__x**2+self.__y**2+self.__z**2)
        return ans
        #********** End *********#



class Vector3d:
    def __init__(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z

    def length(self):
        return (self.__x**2 + self.__y**2 + self.__z**2) ** 0.5

    # 请在这里增加3个特殊方法，分别用来支持加法运算符、减法运算符以实现两个三维向量间的加法和减法运算，以及打印函数print()
        #********** Begin *********#
    def __str__(self):
        return str((self.__x,self.__y,self.__z))

    def __add__(self, v):
        x=self.__x+v.__x
        y=self.__y+v.__y
        z=self.__z+v.__z
        return Vector3d(x,y,z)

    def __sub__(self, v):
        x=self.__x-v.__x
        y=self.__y-v.__y
        z=self.__z-v.__z
        return Vector3d(x,y,z)

        #********** End *********#




def findPayment(loan, r, m):
    #********** Begin *********#
    # 请在下面编写代码
    return loan*((r*(1+r)**m)/((1+r)**m-1))

    # 请不要修改下面的代码
    #********** End *********#
class Mortgage(object):
    def __init__(self, loan, annRate, months):
        #********** Begin *********#
        # 请在下面编写代码
        self.loan=loan
        self.rate=annRate/1200.0
        self.months=months
        self.paid=[0.0]
        self.owed=[loan]
        self.payment=findPayment(loan,self.rate,self.months)
        # 请不要修改下面的代码
        #********** End *********#
        self.legend = None

    def makePayment(self):
        #********** Begin *********#
        # 请在下面编写代码
        self.paid.append(self.payment)
        reduction=self.payment-self.owed[-1]*self.rate
        self.owed.append(self.owed[-1]-reduction)
        # 请不要修改下面的代码
        #********** End *********#

    def getTotalPaid(self):
        #********** Begin *********#
        # 请在下面编写代码
        return sum(self.paid)
        # 请不要修改下面的代码
        #********** End *********#

    def __str__(self):
        return 'The Mortgage is {self.legend}, Loan is {self.loan}, Months is {self.months}, Rate is {self.rate:.2f}, Monthly payment is {self.payment:.2f}'.format(self=self)

if __name__=="__main__":
    print(Mortgage(100000, 6.5, 36))
    print(Mortgage(100000, 6.5, 120))




def findPayment(loan, r, m):
    return loan * ((r * (1 + r) ** m) / ((1 + r) ** m - 1))

class Mortgage(object):
     def __init__(self, loan, annRate, months):
         self.loan = loan
         self.rate = annRate / 1200.0
         self.months = months
         self.paid = [0.0]
         self.owed = [loan]
         self.payment = findPayment(loan, self.rate, self.months)
         self.legend = None

     def makePayment(self):
         self.paid.append(self.payment)
         reduction = self.payment - self.owed[-1] * self.rate
         self.owed.append(self.owed[-1] - reduction)

     def getTotalPaid(self):
         return sum(self.paid)

     def __str__(self):
         return str(self.legend)


class Fixed(Mortgage):
    def __init__(self, loan, r, months):
        # 请在此添加代码，补全函数__init__
        #********** Begin *********#
        self.loan=loan
        self.r=r
        self.months=months
        #********** End *********#
        self.legend = 'Fixed, ' + str(r) + '%, for ' + str(months) + ' months'


class FixedWithPoints(Mortgage):
    def __init__(self, loan, r, months, pts):
        # 请在此添加代码，补全函数__init__
        #********** Begin *********#
        self.loan=loan
        self.r=r
        self.months=months
        self.pts=pts
        #********** End *********#
        self.legend = 'Fixed, ' + str(r) + '%, ' + str(pts) + ' points, for ' + str(months) + ' months'


class TwoRate(Mortgage):
    def __init__(self, loan, r, months, teaserRate, teaserMonths):
        # 请在此添加代码，补全函数__init__
        #********** Begin *********#
        self.loan=loan
        self.r=r
        self.months=months
        self.teaserRate=teaserRate
        self.teaserMonths=teaserMonths

        #********** End *********#
        self.legend = str(teaserRate)\
                      + '% for ' + str(self.teaserMonths)\
                      + ' months, \n then ' + str(r) + '%, for ' + str(months) + ' months'

    def makePayment(self):
        # 请在此添加代码，补全函数makePayment
        #********** Begin *********#


        #********** End *********#
        Mortgage.makePayment(self)

if __name__=="__main__":

    print(Fixed(100000, 6.5, 36))
    print(Fixed(100000, 6.5, 120))

    print(FixedWithPoints(100000, 6.5, 36, 20))
    print(FixedWithPoints(100000, 6.5, 120, 20))

    print(TwoRate(100000, 9.0, 36, 4.8, 12))
    print(TwoRate(100000, 7.0, 120, 4.8, 36))





def findPayment(loan, r, m):
    return loan * ((r * (1 + r) ** m) / ((1 + r) ** m - 1))

class Mortgage(object):
     def __init__(self, loan, annRate, months):
         self.loan = loan
         self.rate = annRate / 1200.0
         self.months = months
         self.paid = [0.0]
         self.owed = [loan]
         self.payment = findPayment(loan, self.rate, self.months)
         self.legend = None

     def makePayment(self):
         self.paid.append(self.payment)
         reduction = self.payment - self.owed[-1] * self.rate
         self.owed.append(self.owed[-1] - reduction)

     def getTotalPaid(self):
         return sum(self.paid)

     def __str__(self):
         return str(self.legend)


class Fixed(Mortgage):
    def __init__(self, loan, r, months):
        Mortgage.__init__(self, loan, r, months)
        self.legend = 'Fixed, ' + str(r) + '%, for ' + str(months) + ' months'


class FixedWithPoints(Mortgage):
    def __init__(self, loan, r, months, pts):
        Mortgage.__init__(self, loan, r, months)
        self.pts = pts
        self.paid = [loan * (pts / 100.0)]
        self.legend = 'Fixed, ' + str(r) + '%, ' + str(pts) + ' points, for ' + str(months) + ' months'


class TwoRate(Mortgage):
    def __init__(self, loan, r, months, teaserRate, teaserMonths):
        Mortgage.__init__(self, loan, teaserRate, months)
        self.teaserMonths = teaserMonths
        self.teaserRate = teaserRate/1200
        self.nextRate = r / 1200.0
        self.legend = str(teaserRate)\
                      + '% for ' + str(self.teaserMonths)\
                      + ' months, \n then ' + str(r) + '%, for ' + str(months) + ' months'

    def makePayment(self):
        if len(self.paid) == self.teaserMonths + 1:
            self.rate = self.nextRate
            self.payment = findPayment(self.owed[-1], self.rate, self.months - self.teaserMonths)
        Mortgage.makePayment(self)


def compareMortgages(amt, years, fixedRate, pts, ptsRate, varRate1, varRate2, varMonths):
    # 请在此添加代码，补全函数compareMortgages
        #********** Begin *********#
        # self.amt=amt
        # self.years=years
        # self.fixedRate=fixedRate
        # self.pts=pts
        # self.ptsRate=ptsRate
        # self.varRate1=varRate1
        # self.varRate2=varRate2
        # self.varMonths=varMonths
    totMonths=years*12
    fixed1=Fixed(amt,fixedRate,totMonths)
    fixed2=FixedWithPoints(amt,ptsRate,totMonths,pts)
    twoRate=TwoRate(amt,varRate2,totMonths,varRate1,varMonths)
    morts=[fixed1,fixed2,twoRate]
        #********** End *********#
    for m in range(totMonths):
        # 请在此添加代码，补全函数compareMortgages
        #********** Begin *********#
        for mort in morts:
            mort.makePayment()
        #********** End *********#
    for m in morts:
        print(m)
        print('Loan ' + str(amt) + ' Total payments = ' + str(int(m.getTotalPaid())))

if __name__=="__main__":
    compareMortgages(200000, 30, 7, 3.25, 5, 4.5, 9.5, 48)
    print('*'*40)
    compareMortgages(1000000, 30, 7, 20, 5, 4.5, 9.5, 48)
    print('*' * 40)
    compareMortgages(500000, 10, 7, 20, 5, 4.5, 9.5, 48)






import specialmethodtest
sc = specialmethodtest.subClass()
# 请在下面填入判断subClass是否为parentClass的子类的代码，并输出结果
########## Begin ##########
print(issubclass(specialmethodtest.subClass,specialmethodtest.parentClass))
########## End ##########
# 请在下面填入判断sc是否为subClass实例的代码，并输出结果
########## Begin ##########
print(isinstance(sc,specialmethodtest.subClass))
########## End ##########
# 请在下面填入判断实例sc是否包含一个属性为name的代码，并输出结果
########## Begin ##########
print(hasattr(sc,"name"))
########## End ##########
# 请在下面填入将sc的属性name的值设置为subclass的代码
########## Begin ##########
setattr(sc,"name","subclass")
########## End ##########
# 请在下面填入获取sc的属性name的值的代码，并输出结果
########## Begin ##########
print(getattr(sc,"name"))
########## End ##########
# 请在下面填入调用subClass的父类的tell()方法的代码
########## Begin ##########
super(specialmethodtest.subClass,sc).tell()
########## End ##########







import Bagtest
price = int(input())
bag = Bagtest.Bag(price)
# 请在下面填入输出Bag类中变量__price的代码
########## Begin ##########
print(bag._price)
########## End ##########
# 请在下面填入输出Bag类中变量_price的代码
########## Begin ##########
print(bag._price)
########## End ##########






class WrapClass(object):
    def __init__(self,obj):
        self.__obj = obj
    def get(self):
        return self.__obj
    def __repr__(self):
        return 'self.__obj'
    def __str__(self):
        return str(self.__obj)
    # 请在下面填入重写__getattr__()实现授权的代码
    ########## Begin ##########
    def __getattr__(self,thelist):
        return getattr(self.__obj,thelist)
    ########## End ##########


thelist = []
inputlist = input()
for i in inputlist.split(','):
    result = i
    thelist.append(result)
# 请在下面填入实例化类，并通过对象调用thelist，并输出thelist第三个元素的代码
########## Begin ##########
wp=WrapClass(thelist)
wp_list=wp.get()
print(wp_list[2])


########## End ##########


import delObjecttest

# 请在下面声明类delObject的实例，并将其引用赋给其它别名，然后调用del方法将其销毁
########## Begin ##########
do = delObjecttest.delObject()
del (do)

########## End ##########


import animalstest
# 请在下面填入定义fish类的代码，fish类继承自animals类
########## Begin ##########
class fish(animalstest.animals):
########## End ##########
    def __init__(self,name):
        self.name = name
    def swim(self):
        print("%s会游泳" %self.name)

# 请在下面填入定义leopard类的代码，leopard类继承自animals类
########## Begin ##########
class leopard(animalstest.animals):
########## End ##########
    def __init__(self,name):
        self.name = name
    def climb(self):
        print("%s会爬树" %self.name)

fName = input()
lName = input()
f = fish(fName)
f.breath()
f.swim()
f.foraging()
l = leopard(lName)
l.breath()
l.run()
l.foraging()


class Point:
    def __init__(self, x, y, z, h):
        self.x = x
        self.y = y
        self.z = z
        self.h = h

    def getPoint(self):
        return self.x, self.y, self.z, self.h


class Line(Point):
    # 请在下面填入覆盖父类getPoint()方法的代码，并在这个方法中分别得出x - y与z - h结果的绝对值
    ########## Begin ##########
    def getPoint(self):
        length_one = abs(self.x - self.y)
        length_two = abs(self.z - self.h)
        ########## End ##########
        print(length_one, length_two)









class ChangeAbs(int):
    def __new__(cls, val):
        # 填入使用super()内建函数去捕获对应父类以调用它的__new__()方法来计算输入数值的绝对值的代码
        # 求一个数的绝对值的函数为abs()
        # 返回最后的结果
        ########## Begin ##########
        return abs(val)
        ########## End ##########

class SortedKeyDict(dict):
    def keys(self):
        # 填入使用super()内建函数去捕获对应父类使输入字典自动排序的代码
        # 返回最后的结果
        ########## Begin ##########
        return sorted(super(SortedKeyDict, self).keys())
        ########## End ##########



class A(object):
    def test(self):
        print("this is A.test()")
class B(object):
    def test(self):
        print("this is B.test()")
    def check(self):
        print("this is B.check()")
# 请在下面填入定义类C的代码
########## Begin ##########
class C(A):
########## End ##########
    pass
# 请在下面填入定义类D的代码
########## Begin ##########
class D(A):
########## End ##########
    def check(self):
        print("this is D.check()")
class E(C,D):
    pass




