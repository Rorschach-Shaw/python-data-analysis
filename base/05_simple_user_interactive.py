# 简单用户交互


# 语法： variable = input(提示词) input的返回值一定是字符串
var_a = input("输入一个数字:")
var_b = input("输入另外一个数字:")
print(var_a + var_b)

# 使用type 来查看一个变量的类型
print(type(var_a))

# 字符串转换成其他类型
# python基础数据类型：
# 想把 谁 转化成目标类型，就把 它 用目标类型括起来

var_c = int(var_a)
print(var_c)
print(type(var_c))