def return_tuple():
    name = "jack"
    province = "usa"
    # return (name,province)
    return name, province  # 如果函数返回的是元组,就可以省略括号


info_tuple = return_tuple()  # 返回的是一个元组
gl_name, gl_province = return_tuple()  # 使用多个变量接收结果

a = 1
b = 2
a, b = b, a  # 交换a与b的值

"""
  在对列表变量进行+=操作时会调用列表的extend方法,不会改变列表变量的引用;
  其他变量则是先+再赋值,会改变引用.
"""
gl_num = 10
gl_list = [1, 2, 3, 4]


def change_value(num, list):
    num += num  # num = num +num
    list += list  # list.extend(list)
    print("函数内部:")
    print(num)
    print(list)


change_value(gl_num, gl_list)  # 函数改变了列表的值,但没有改变数字的值
print("函数外部:")
print(gl_num)
print(gl_list)

"""
  函数的多值参数,一般元组类型的是:*args;字典类型的是:**kwargs;
  可以使用for in 遍历多值参数
"""


def multi_value(num, *args, **kwargs):
    print(num)
    print(args)
    print(kwargs)


multi_value(1, 2, 3, 4, 5, name="", age=18, gender=True)  # multi_value(1,(2,3,4,5),{'name': '','age':18,'gender':True})
args_tuple = (1, 2, 3, 4)
args_kwargs = {'name': 'jack', 'age': 18, 'gender': True}
multi_value(1, *args_tuple, **args_kwargs)  # 拆包调用,标识,不然会将两个变量参数当成元组的成员


def add(num):
    """
    数字累加,递归函数
    :param num:
    :return:
    """
    if num == 1:
        return 1
    return num + add(num-1)


print(add(2))
