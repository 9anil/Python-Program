a,b=input().split()
a=int(a)
b=int(b)
c=input()
arr=[1,2,3,4]
try:
    # print(a//b)
    # print(a+b+c)
    # print(a+d)
    print(arr[10])
# except Exception:
#     print("Diviser number not allowed 0")
except Exception as e:
    print(e)
finally:
    print("This statement print in every case!")