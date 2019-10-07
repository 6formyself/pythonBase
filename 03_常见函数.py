import random
# 输入函数
a = input("please input your password")  # input返回值是str

# 类型转换函数
b = int("123")
c = float("12.3")
d = bool("aaa")  # 非0的任意内容都是True
print(b, c, d)

# 随机数
f = random.randint(10, 20)  # 10 <= f <= 20
print(f)
