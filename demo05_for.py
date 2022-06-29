# for 循环
"""""
for 循环变量 in 序列：
    执行代码块
"""""
# 需求：循环字符串abcde中的每个字符
for x in "abcde":
    print(x)

# while 循环
"""""
初始值
while 条件语句：
    执行代码块
"""""
# 需求：打印1-5的数
for y in "12345":
    print(y)

a = 1
while a <= 5:
    print(a)
    a += 1

# 需求：计算1-100的和
sum = 0
for x in range(0, 101):
    sum += x
print(sum)

sum1 = 0
i = 0
while i <= 100:
    sum1 += i
    i += 1
print(sum1)
