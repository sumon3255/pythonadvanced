#File io in python

#modes

# 'r' - open for reading
#'w' - open for writing
#'x' - open for exclusive creation
# 'a' append to the end of file
#'b' binary mode
#'t' text mode (default)
# '+' simultinously read or write


#open a file
# open('filename','r')

#Read a file
# f = open('myfile.txt',"rt")
#
# a = f.read()
# print(a)
# f.close()

#read line by line

# f = open('myfile.txt')
# #
# # for line in f:
# #     print(line)
# #
# # f.close()

#writing and appending
f = open('myfile2.txt',"a")

a = f.write("I am sumon")
# print(a)
f.close()

#read and write both
#
# f = open('myfile2.txt',"r+")
#
# print(f.read())
# a = f.write("this is the end")
# # print(a)
# f.close()

#tell()

# f = open("myfile2.txt")
# print(f.tell())
# print(f.readline())
# print(f.tell())
# print(f.readline())
# print(f.tell())
# print(f.readline())
# print(f.tell())
#
# f.close()

#seek()

# f = open("myfile2.txt")
# print(f.seek(10))
# print(f.readline())
#
# print(f.readline())
#
# print(f.readline())
#
#
# f.close()

#using with block

# with open("myfile2.txt") as f:
#     a = f.readline()
#     print(a)
