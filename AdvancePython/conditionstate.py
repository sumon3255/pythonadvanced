# a =7
# b = 70
# c = int(input("Enter a number\n"))
# if c > b:
#     print("Greater")
# elif c == b:
#     print("equal")
# else:
#     print("lesser")

lst = [1,5,7,3]
# print(3 not in lst)
# if 3 in lst:
#     print("Yes 3 is in the lst ")
#
# else:
#     print("sorry it is not in the list")


#Quiz
#practise vote eligibility

print("Enter Your age")
age = int(input())
if age<17:
    print("You are not eligible for vote")
elif age==17:
    print("Wait few more days")
elif age>17:
    print("You are  eligible for vote")
else:
    print("Enter a Valid age")