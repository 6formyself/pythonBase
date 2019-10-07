# 1.数字型
a: int = 1  # python3去除了long类型
b: float = 1.1
c: bool = True  # 非0就是True，0为False
d: complex = 2  # 复数型

# 2.非数字型
# 2-1:字符串
e: str = ("1" + "2") * 10  # 10个12 数字不能和字符串进行普通的运算
char = e[1]
substr = e[1:4]  # 字符串切片
substr2 = e[1::2]  # 步长,从一开始每隔两个截取一个直到最后
substr3 = e[-1::-1]  # 倒序e[::-1]
# 2-2:列表,就是数组
name_list = ["张三", "王五", "小明", "李四"]
len(name_list)  # 获取列表长度
name_list.count("张三")  # 数据在列表中出现的次数
name_list.sort()  # 列表升序排序
name_list.sort(reverse=True)  # 列表降序排序
name_list.reverse()  # 列表反转
name_list.append("王五")
name_list.insert(1, "小明")
name_list.extend(name_list)  # 把其他列表的数据加入当前列表
little_list = name_list[1:3]  # 列表切片
del name_list[1]  # 从内存中删除
for item in name_list:
    print(item)
else:
    print("for in else")  # 集合从头到尾遍历一遍后才会执行.如果for中使用了break,该代码块就不会执行.
# 2-3:元组
name_tuple = ("李四", 18, 1.75)  # 元组一旦定义完成就不能修改;1.函数多个返回值;2.格式字符串;保护列表不被修改
print("%s的年龄是%d,身高是%.2f" % name_tuple)
name_str = "%s的年龄是%d,身高是%.2f" % name_tuple
single_tuple = (5,)  # 一个元素的元组
for item in name_tuple:
    print(item)
list(name_tuple)  # 列表跟元组的转换函数
tuple(name_list)
little_tuple = name_tuple[1:3]  # 元组切片
# 2-4:字典
member_info = {"name": "小明", "age": 18, "height": 1.75, "gender": True}  # 类似json数据格式
name = member_info["name"]
len(member_info)  # 统计键值对的数量
for key in member_info:
    print("%s : %s" % (key, member_info[key]))

# 3.变量的格式化输出-- %s：字符串，%d：有符号十进制整数，%f：浮点数（%.02f：小数后两位），%%：输出%
price = "9.5"
weight = "3"
print("苹果的单价为：%.03f元/斤，购买的数量为：%.02f斤" % (float(price), float(weight)))
student_nu = 1
print("the student number is %06d" % student_nu)  # %06d：输出整数的格式，不足用0补
scale = 0.1
print("the scale is %.2f%%." % (scale * 100))

