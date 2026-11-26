# day_3
# VACAEX_question_1
x, y = map(int, input().split())
print(y+x-1)
# MISSINGNUM7_question_2
s = int(input())

if s == 6:
    print(4)
elif s == 7:
    print(3)
elif s == 8:
    print(2)
else:
    print(1)
# CLSI_question_3
n, b = map(int, input().split())
if n >= (10*b):
    print("yes")
else:
    print("no")
# GAMBLING_question_4
a = int(input())
print(7-a)
# FAVWD_question_5
s = input().strip()
if s[0] == "c" or s[-1] == "f":
    print("yes")
else:
    print("no")
# SQUIDBANK_question_6
n, k = map(int, input().split())
print((n-k)*10000)
# EXGS_question_7
x, y = map(int, input().split())
print((x*100)+((y-x)*150))
# TRICHECK_question_8
a, b, c = map(int, input().split())
if a+b > c and b+c > a and a+c > b:
    print("yes")
else:
    print("no")
# AICOM_question_9
x = int(input())
if x <= 60:
    print("yes")
else:
    print("no")
# CWCTH_question_10
a, b = map(int, input().split())
if b >= a*3:
    print("rain")
else:
    print("dry")
