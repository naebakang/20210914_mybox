class Foo:
    def __init__(self):
        self.x = 5
    
    def func1():
        print("function 1")
        
    def func2(self):
        print(id(self))
        print("function 2")


f = Foo()
print(id(f))
f.func2()
Foo.func1()
Foo.func2(3)


class Stock:
    market = "kospi"

print(dir())

print(Stock.__dict__)

print(Stock.market)

s1 = Stock()
s2 = Stock()
print(id(s1))
print(id(s2))

print(s1.market)
s1.market = 'kisdaq'
print(s1.market)
print(s1.__dict__)
print(s2.__dict__)

#print(s2.volume)



# class 내 변수에 관한 고찰, class가 앞에 붙어야 class 내 함수에서 동일한 변수가 작동된다.
class Account:
    num_accounts = 0
    def __init__(self, name):
        self.name = name
        Account.num_accounts += 1
    def __del__(self):
        Account.num_accounts -= 1

kim = Account("kim")
lee = Account("lee")

print(kim.num_accounts)
print(Account.num_accounts)

class Account_b:
    num_accounts = 0
    def __init__(self, name):
        print('init 실행 시작')
        self.name = name
        num_accounts = 0
        num_accounts += 1
        print(num_accounts)
        print('init 실행 끝')
    def __del__(self):
        num_accounts -= 1

kim_b = Account_b("kim")
lee_b = Account_b("lee")

print(kim_b.num_accounts)
print(Account_b.num_accounts)
