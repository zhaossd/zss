# #三天打鱼两天晒网
# year,month,day = eval(input("请输入年月日（用逗号分开）："))#获取输入数据
# monthdays = [31,28,31,30,31,30,31,31,30,31,30,31]
# #每月天数
# if year <= 0 :
#     print("年不合法")
# else:
#     if(year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         monthdays[1]=29
#     if month>12 or month<1:
#         print("月份不合法")
#     elif day <1 or day > monthdays[month-1]:
#         print("日不合法")
#     else:
#         if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#             monthdays[1] = 29
#         count = 0
#         for i in range(month-1):
#             count+=monthdays[i]
#         count+=day
#
#         if count %5 in[1,2,3]:
#             print("小明在打鱼")
#         else:
#             print("小明在晒网")

#
#
# #大小写转换
# num = input("请输入一个字母：")
# if 'a'<=num<='z':
#     print(num.upper())
# elif 'A'<=num<='Z':
#     print(num.lower())
# else:
#     print(num)

#


#################12题：
# list = ["张三","李四","王五","赵六","孙七","周八","吴九"]
# odd_name = []#奇数
# even_name = []#偶数
# for index,name in enumerate(list,start=1):#将一个可迭代对象组合为一个索引序列，同时返回索引和对应元素
#     if index %2 ==1:
#         odd_name.append(name)
#     else:
#         even_name.append(name)
#
# print("分组\t\t1\t2\t3\t4")
#
# print("奇数组\t"+"\t".join(odd_name))
# print("偶数组\t"+"\t".join(even_name))
#

##############17题：
# n = int(input("请输入一个整数："))
# is_prime = [True]*n
# is_prime[0]=is_prime[1]=False
# for i in range(2,int(n**0.5+1)):
#     if is_prime[i]:
#          for j in range(i*i,n,i):
#              is_prime[j] = False
# for i in range(n):
#     if is_prime[i]:
#         print(i,end= '\t')
#


#
# #########18题：
# n = int(input("Please input the number of rows:"))
# m = int(input("Please input the number of columns:"))
# A = []
# for i in range(n):
#     row = []
#     for j in range(m):
#         num = int(input(f"Please input A[{i},{j}]"))
#         row.append(num)
#     A.append(row)
# B = []
# for i in range(n):
#     row = []
#     for j in range(m):
#         num = int(input(f"Please input B[{i},{j}]"))
#         row.append(num)
#     B.append(row)
# C = []
# for i in range(n):
#     row = []
#     for j in range(m):
#         row.append(A[i][j]+B[i][j])
#     C.append(row)
# print(f"C={C}")
#


####################19题：

H = float(input("请输入初始高度："))
N = int(input("请输入下落次数："))

total = H
for i in range(1,N):
    total += 2*(H/(2**i))#每次加2倍H/2
rebound_height = H/2**N
print(total)
print(rebound_height)
