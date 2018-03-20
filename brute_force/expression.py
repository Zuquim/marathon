# http://codeforces.com/problemset/problem/479/A
a = 0
b = 0
c = 0
while a < 1 or a > 10:
    a = int(input())
while b < 1 or b > 10:
    b = int(input())
while c < 1 or c > 10:
    c = int(input())
u = a + b + c
v = a + b * c
w = a * b + c
x = a * (b + c)
y = a * b * c
z = (a + b) * c
r_list = [u, v, w, x, y, z]
r_list.sort()
highest = r_list.pop()
print('a: {0}\nb: {1}\nc: {2}\n'.format(a, b, c))
print(highest)
