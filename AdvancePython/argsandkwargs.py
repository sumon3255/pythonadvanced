#*args And **kwargs

# def func1(a,b,c,d,e):
#     print(a,b,c,d,e)
#
# func1("sumon","galib","nerob","kamrul","junaed")

def myfunargs(a,*args,**kwargs):
    for item in args:
        print(item)
    print("Now lets talk about their positions")
    for key,value in kwargs.items():
        print(f"{key} position is {value}")


playerlist = ["sumon","galib","nerob","kamrul","junaed","saad"]

a = "This is normal argument"

dic = {"sumon":"DMF","Galib":"CB","nerob":"Lwf","kamrul":"CMF"}
myfunargs(a,*playerlist,**dic)