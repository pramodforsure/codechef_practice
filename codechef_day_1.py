# day_1
# NYRES_question_1
x = int(input())
pushups = x*31
print(pushups)
# POINTCAL_question_2
a, b, c = map(int, input().split())
noOfPoints = a*3+b*1+c*0
print(noOfPoints)
# POPCORN7_question_3
X = int(input())
buckets = (X - 100) // 50
print(buckets)
# LMP1_question_4
x, y = map(int, input().split())
if x >= y:
    print("yes")
else:
    print("no")
# REGCLN_question_5
n = int(input())

ld = n % 10
days = 10-ld
print(days)
# SANDWSHOP_question_6
a, b, c = map(int, input().split())
print(a-(b+c))
# WAPEN_QUESTION_7
x, y = map(int, input().split())
print(x+(y*10))
# EXREST_question_8
n = int(input())
print(3*n)
# TRIANGLE7_question_9
a, b = map(int, input().split())
print(180-(a+b))
# ODDPWD_question_10
s = input().strip()
print(s[0] + s[2] + s[4])
