#Generators

'''
Iterable - __iter__() or __getitem__()
Iterator - __next__()
Iteration

'''

#Generator

# for i in range(505):
#     print(i)
#
# def gener(n):
#     for i in range(n):
#        yield i
#
#
# g =  gener(4)
# # print(g.__next__())
# # print(g.__next__())
# # print(g.__next__())
# # print(g.__next__())
# #
# # for i in g:
# #     print(i)
#
# h = "Sumon"
#
# iter1 = iter(h)
# print(iter1.__next__())
# print(iter1.__next__())
# print(iter1.__next__())
#
# # for i in h:
# #     print(i)

#
# def fib(limit):
#     a,b =0,1
#
#     while a < limit:
#         yield a
#         a,b = b, a+b
#
# x = fib(5)
#
# # print(x.__next__())
# # print(x.__next__())
# # print(x.__next__())
# # print(x.__next__())
# # print(x.__next__())
#
# for i in fib(5):
#     print(i)
#


#Comprehensions in python

# lst = []

# for i in range (100):
#     if i%5 == 0:
#         lst.append(i)
#
# print(lst)
# lst = [i for i in range(100) if i%5 == 0]
# print(lst)


#dct = {i:f"item {i}" for i in range(1,1000) if i%5==0 }

#print(dct)

# dct = {i:f"item {i}" for i in range(10)}
# print(dct)
# dct1 = {value:key for key,value in dct.items()}
# print(dct1)

# def mygernrator(n):
#     for i in range(n):
#         yield i
#
# x = mygernrator(5)
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
#
# mygernrator = (i for i in range(100) if i%2 == 0)
# print(mygernrator.__next__())
# print(mygernrator.__next__())
# print(mygernrator.__next__())
#
# mygernrator = (i for i in range(100) if i%2 == 0)
# print(mygernrator.__next__())
# print(mygernrator.__next__())
# print(mygernrator.__next__())

#Else with for loop

# friend_lst = ["sumon","galib","kamrul"]
#
# for item in friend_lst:
#     if item == "nerob":
#         break
#
#
# else:
#     print("This is else with foor loop")

# #Function caching in python
# import time
# from functools import lru_cache
# @lru_cache(maxsize=20)
# def func1(n):
#     time.sleep(n)
#     return n
# if __name__ == '__main__':
#     print("...strating..")
#     func1(4)
#     func1(5)
#     func1(6)
#     func1(7)
#
#     print("..Done... calling again")
#     input()
#     func1(4)
#     print("calling again")


#Coroutines in python
#Generators are data producers
#Coroutines are data conjumers

# def feb():
#     a, b = 0,1
#     while True:
#         yield a
#         a , b = b, a + b
# for i in feb():
#     print(i)

# def grep(pattern):
#     print("Serching for", pattern)
#     while True:
#         line = (yield )
#         if pattern in line:
#             print(line)
#
# search = grep('coroutines')
# next(search)
# search.send("I love you")
# search.send("Don't you love me")
# search.send("I love coroutines instead")
#
# search.close()

#Else , Finally , Try and Except

# try:
#     f = open("galib2.txt")
# except EOFError as e:
#     print("We found Eoferror",e)
# except IOError as e:
#     print("We found Ioerror",e)
#
# else:
#     print("This will run if except is not running")
#
# finally:
#     print("Run this anyway")
#     # f.close()

#Os module in python
import os
# print(dir(os))
# print(os.getcwd())
# os.chdir("H://")
# # print(os.getcwd())
# print(os.listdir())

# os.mkdir("Sumon")
# os.makedirs("sumon/me")
# os.rename("galib.txt","galib2.txt")
# print(os.environ.get('Path'))
# print(os.path.join("H:/","/glaib2.txt"))
# print(os.path.exists("C://Program Files2"))

# print(os.path.isfile("galib2.txt"))

#Request module in python
import requests
# r = requests.get("https://www.7timer.info/bin/astro.php?lon=113.2&lat=23.1&ac=0&unit=metric&output=json&tzshift=0%27=")
# # print(r.status_code)
# print(r.text)

# url = "www.xyx.com"
# data = {
#     "name":"sumon",
#     "age":21
# }
#
# r2 = requests.post(url=url,data=data)
#Json in python
import json

# data = '{"Name1":"SUMON","Name2":"Galib"}'
# print(data["Name1"])
# parsed = json.loads(data)
# print(parsed["Name1"])

# f = open('myfile.json')
#
# data = json.load(f)
# # for i in data:
# #     print(i)
# # print(data['fruit'])
# f.close()

#dumps in json

# data2 = {
#     "GroupName":"Xyz",
#     "Members":["sumon","galib","kamrul"],
#     "Items":("banana",10),
#     "bdhabit":False
# }
#
# a = json.dumps(data2)
# print(a)

#pickle Module
import pickle
# Picking a python object

# friend_list = ["galib","kamrul","nerob","junaed"]
# file = "myfriendlst.pkl"
# fileobj = open(file,'wb')
# pickle.dump(friend_list,fileobj)
# fileobj.close()


# file = "myfriendlst.pkl"
# fileobj = open(file,'rb')
# myfriends = pickle.load(fileobj)
# print(myfriends)
# print(type(myfriends))

#Regular expressions
import re

string_template = '''XYZ Limited
Md Galib, executive director
18, Dhaka 1206
Bangladesh
Phone: +880 1714296673
Fax: +880 1714296673
Email: xyz.34@gmail.com
Website: www.exyz.com

Uttara Dhaka , 
DHAKA 1230

Phone: +88 0164-35373636
Fax: +88 016435373636
Email: xyz.ac.bd.com 
Website: www.abcd.com
So lets learn about regular expressiions in python'''

#findall #search # split # sub
# a = re.compile(r".earn")
# a = re.compile(r"^XYZ")
# a = re.compile(r"python$")
# a = re.compile(r"si*")
# a = re.compile(r"si+")
# a = re.compile(r"si{2}")
# a = re.compile(r"(si){1}")
# a = re.compile(r"si{2}|t")

#special sequences
# a = re.compile(r"\AXYZ")
# a = re.compile(r"\bFax")
# a = re.compile(r"30\b")
# a = re.compile(r"\d{4}-\d{5}")
# macthes = a.finditer(string_template)
# for match in macthes:
#     print(match)
    # print(string_template[268:272])

# s = """Hello from shubhamg199630@gmail.com
#         to priya@yahoo.com about the meeting @2PM"""
#
# lst = re.findall("\S+@\S+",s)
# print(lst)

# Loops inside Loop

# adj = ["red","big","tasty"]
# fruits  = ["apple","banana","cherry"]
#
# for i in adj:
#     for j in fruits:
#         print(i,j)

# Nested conditional statements

# num =  float(input("Enter a number"))
# if num >=0:
#     if num == 0:
#         print("zero")
#     else:
#         print("Positive Number")
# else:
#     print("Negative Number")

#Add Two Numbers in mattrix
X = [[1,2,3],
     [4,5,6],
     [7,8,9]]

Y=[[9,8,7],
     [6,5,4],
     [3,2,1]]

result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

#itrate through row
for i in range(len(X)):
    # itrate through Column
    for j in range(len(Y)):
        result[i][j] = X[i][j] + Y[i][j]

for i in result:
     print(i)



