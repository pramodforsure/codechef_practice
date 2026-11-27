# day_4
# REMMON_question_1
n, a, b = map(int, input().split())
print(n-(a*b))
# NOTECNT_question_2
a, b = map(int, input().split())
print((a*b)*100)
# EXUNPIZZA_question_3
n, k, r = map(int, input().split())
print((n-k)*r)
# P119_question_4
x = int(input())
if x >= 10:
    print("yes")
else:
    print("no")
# FOODCOST_question_5
x, y = map(int, input().split())
print((x*6)+y)
# PZSPILT_question_6
n = int(input())
if n % 2 == 0:
    print(1)
else:
    print(2)
# P1235_question_7
x, y = map(int, input().split())
if y <= x:
    print(0)
else:
    print(100)
# IOI7_question_8
n, g = map(int, input().split())
if n >= g:
    print("yes")
else:
    print("no")
# NUGGET_question_9
x, y = map(int, input().split())
print((x*5000)+(y*9800))
# EQICHOC_question_10
r, l = map(int, input().split())
maxx = max(r, l)
minn = min(r, l)
print(maxx-minn)
