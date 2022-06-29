# 列表推导式 ：[ 表达式2 循环体 表达式1]，执行的顺序：先执行循环体，其次执行后面的额表达式1，最后执行表达式2

# 需求1 ：生成一个1-10的列表
lst = []
for x in range(1, 11):
    lst.append(x)
print(lst)

lst2 = [x for x in range(1, 11)]
print(lst)

# lst1 = []
# for x in range(1, 11):
#     lst1.append(x)
# print(lst1)
#
# lst2 = [x for x in range(1, 11)]
# print(lst2)

# 需求2 ：生成一个1-10的列表,需求只打印奇数的值
lst3 = [x for x in range(1, 11) if x % 2 != 0]
print(lst3)

lst3 = []
for x in range(1, 11, 2):
    lst3.append(x)
print(lst3)

lst3 = []
for x in range(1, 11):
    if x % 2 != 0:
        lst3.append(x)
print(lst3)

lst4 = [x for x in range(1, 11) if x % 2 != 0]
print(lst4)

# 需求3 ：生成一个1-10的列表,需求打印奇数的值加10
lst5 = [x + 10 for x in range(1, 11) if x % 2 != 0]
print(lst5)
