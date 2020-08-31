# 分支语句 if elif else
a = int(input("请输入a的值："))
if 1 <= a < 10:
    print("a大于1并且a小于10")
elif 10 <= a < 20:
    print("a大于10并且a小于20")
else:
    print("a大于20")
# 逻辑运算符：与and（相当于&&）/或or（相当于||）/非not（相当于！）

# 循环语句
i = 1
result = 0
while i <= 100:  # 1-100的和
    if i % 2 == 0:
        result += i
    i += 1  # i = i+1
print(result)

i = 1
while i <= 9:  # 99乘法表
    j = 1
    while j <= i:
        print("%d*%d=%d\t" % (j, i, i * j), end="")  # 避免换行
        j += 1
    print("\n")
    i += 1

i = 1
while i <= 9:  # 星星相乘
    print("*" * i)
    i += 1

s = ""
i = 1
while i <= 9:  # 星星打印
    s += "*"
    print(s)
    i += 1
