try:
    a = int(input("Enter your number : "))
    print(a+2)
except Exception as e:
    print("some error occured : \n",e)
except:
    print("Some error occured.")