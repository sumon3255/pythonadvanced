# #if name == '__main__'
#
# def describe(str):
#     print(f"My name is {str}")
# print(f"this is {__name__}")
#
# def addnum(a,b):
#     return a+b;
#
# if __name__ == '__main__':
#
#     describe("sumon")
#     x = addnum(10,20)
#     print(x)


#join function
#
# lst = ["sumon","galib","nerob","kamrul","junaed"]
#
# # for item in lst:
# #     print(item, "and" , end= " ")
#
#
# x = " , ".join(lst)
# print(x)
#
# map() , filter(), reduce()
num = ["1","2","3"]
num = list(map(int,num))
# print(num)

# for i in range(len(num)):
#     num[i] = int(num[i])

num[2] = num[2] +1
# print(num[2])

# def starts_with_A(s):
#     return s[0] == 'A'
#
# fruit = ["Apple","Banana","Pear","Apricot","Oranage"]
#
# map_objet = list(map(starts_with_A,fruit))
# print(map_objet)



# fruit = ["Apple","Banana","Pear","Apricot","Oranage"]
#
# map_objet = list(map(lambda s:s[0]=="A",fruit))
# print(map_objet)

# def square(a):
#     return a*a
# def cube(a):
#     return a*a*a
#
# func1 = [square, cube]
#
# for i in range(5):
#     val = list(map(lambda x:x(i) ,func1))
#     print(val)

#filter()
# def starts_with_A(s):
#     return s[0] == 'A'

# fruit = ["Apple","Banana","Pear","Apricot","Oranage"]
#
# map_objet = list(filter(lambda s:s[0]=="A",fruit))
# print(map_objet)


#reduce()
from functools import reduce

list = [2,4,7,3]

# num = 0
# for i in list:
#     num = num + i
# print(num)

print(reduce(lambda x,y:x + y,list))

