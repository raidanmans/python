str_length = input("please enter the length : ")
str_width = input("please enter the width : ")
str_money = input("how much for one meter : ")
int_length = int(str_length)
int_width = int(str_width)
int_money = int(str_money)
area = int_length * int_width
price = int_money * area
print("the total area : " + str(area) +"m" )
print("the total price : $" + str(price))
# ________________________________________________________________________
length = float(input("please enter the length : "))
width = float(input("please enter the width : "))
money = float(input("how much for one meter : "))
print(f"the total area : {round(length * width,2)}m " )
print(f"the total price : {round(money * (length*width),2)}$")
