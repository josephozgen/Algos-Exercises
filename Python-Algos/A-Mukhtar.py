x = [9, 10, 6, 12]
y = []
for element in x:
    y.append(element+2)
print(y)

names = ['Yusuf', 'Yunus', 'Neslihan', 'Dilara']
for name in names:
    print(name, len(name))
    if len(name)%2==0:
        print('Hello', name)
    else:
        print('Hi', name)

x = (5, 7)
y = 10,
z = (7, 10)
print(type(x) == type(y) == type(z))

A = {'Sam', 'Sarah', 'Zoe'}
B = {'Sam', 'Martin','Catherine','Zoe'}
print(A&B)
print(A-B)
print(A|B)
print(B^A)

print([i for i in range(20) if i%4==False])

str = 'reiiowjojgje'
y = lambda x: 'even' if len(x)%2==0 else 'odd'
print(y(str))

numbers = [1,2,3,7,9,18]
def odd(x):
    return x%2==1
print(list(filter(odd, numbers)))
print(list(map(odd, numbers)))

# How do we add varying number of numbers?
def myAdd(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum
print(myAdd(6,9,10,7,16))

# Try-except block
def getHalf(x):
    try:
        return 0.5*x
    except:
        return 'Best Joke!'
print([getHalf(item) for item in [2,'abc',100,'zzz']])