# NEWYEAR_QUESTION_1
x = int(input())
tt = 24  # tt=total time
tl = x % 24
t = tt-tl
print(t)
# P1_175-question_2
x, y = map(int, input().split())
if x <= y:
    print("yes")
else:
    print("no")
# SHOM_question_3
l, r = map(int, input().split())
if l == r:
    print(0)
if l != r:
    if l > r:
        print(l-r)
    else:
        print(r-l)
# DISCOUNT7_question_4
n = int(input())
if n >= 5:
    print(n*85)
else:
    print(n*100)
# SAMESIT_question_5
x = int(input())

if x % 5 != 0:
    print("YES")
else:
    print("NO")
# TELHOME_question_6
d, t = map(int, input().split())
if d <= t:
    print(0)
else:
    print(d-t)
# BOP1_question_7
x, y = map(int, input().split())
if x > y:
    print("Alice")
elif x < y:
    print("Bob")
else:
    print("Draw")
# SQPAPER_question_8
a, b = map(int, input().split())
s = min(a, b)
print(s*s)
# RECSQ_question_9
a, b, c = map(int, input().split())
if (a*b) == (c*c):
    print("yes")
else:
    print("no")
# VACAEX_question_10
n = int(input())
tt = 600-n*30
print(tt//30)
#this day 2 of consistently uploading my progress

