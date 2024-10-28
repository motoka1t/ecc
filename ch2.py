from Point import *

#2.2
#p1 = Point(-1, -1, 5, 7)
#p2 = Point(-1, -2, 5, 7)

#練習問題1
def on_curve(x,y):
    return y**2 == x**3 + 5*x + 7
print(on_curve(2,4))
print(on_curve(-1,-1))
print(on_curve(18,77))
print(on_curve(5,7))

#2.5
p1 = Point(-1, -1, 5, 7)
p2 = Point(-1, 1, 5, 7)
inf = Point(None, None, 5, 7)
print(p1+inf)
print(inf+p2)
print(p1+p2)

#練習問題4
x1,y1 = 2,5
x2,y2 = -1,-1
s = (y2 - y1)/(x2-x1)
x3 = s**2 - x1 - x2
y3 = s*(x1-x3)-y1 
print(x3,y3)

#練習問題6
a = 5
x1,y1 = -1,-1
s = (3*x1**2+a)/(2*y1)
x3 = s**2-2*x1
y3 + s*(x1-x3)-y1
print(x3,y3)