def first_function():
    """
    第一个函数
    :return: 10
    """
    print(1000)
    return 10


def sum_number(num1, num2):
    """
    两个数字之和
    :return:
    """
    return num1 + num2


first_function()
print(sum_number(10, 20))  # F1查看函数详细信息
for i in range(1, 4):  # i=1;i<4;i++
    print(i)
"""
  函数内部不允许修改全局变量,同名变量只能是局部变量,并不会改变全局变量
  使用global关键字,
  num = 10
  def demo():
     global num
     num = 10  # num被修改为10
  全局变量定义在所有函数上方,全局变量名前应该加上g_,gl_
"""

# %-18s:左对齐打印,总长度为18字符.
print("%-18s\t\t%-18s\t\t%-18s\t\t" % ("name", "qq", "phone"))
print("%-18s\t\t%-18s\t\t%-18s\t\t" % ("Jho man", "22323424324", "132233432342"))
