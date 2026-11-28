# day_5
# FUELCHK_question_1
x, y = map(int, input().split())
if x*y >= 100:
    print("yes")
else:
    print("no")
# HWFIN_question_2
x, y = map(int, input().split())
print("yes" if (x+(y*10) >= 100) else "no")
# IDESM_question_3
n = int(input())
if n == 15:
    print("yes")
else:
    print("no")
# ECHOECHO_question_4
s = input().strip()
if len(s) > 4:
    print("no")
if s[0] == s[2] and s[1] == s[3]:
    print("yes")
else:
    print("no")
# CLEARDAY_QUESTION_5
x, y = map(int, input().split())
print(7-(x+y))
# THALA7_question_6
n = int(input())
print("THALA" if n == 7 else "SADGE")
# LUCLO_question_7
n = int(input())
print(4+((n-1)*3))
# GDTURN_question_8
t = int(input())
for i in range(0, t):
    x, y = map(int, input().split())

    if (x+y) > 6:
        print("yes")
    else:
        print("no")
