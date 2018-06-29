import Menu

class meal(Menu.Brg,Menu.Bev,Menu.Des,Menu.SW):
    bill = 0
    tax = 0.12
    def __init__(self,name,price,qty):
        self.name=name
        self.price=price
        self.qty=qty
    @classmethod
    def Show(cls,ols):
        bill=0
        tax=0.12
        for i in ols:
            bill=bill+(i.price*i.qty)
        total=bill+(0.12*bill)
        print("Your Total bill is:: ",total)
    def __repr__(self):
        message="Name: {}, 1Price: {}, Quantity: {}".format(self.name,self.price,self.qty)
        return message


ordrs=[]
flag=True
print("We have the following List of Items::")
print("Enter 1 for Burgers.")
print("Enter 2 for Deserts.")
print("Enter 3 for Side Wraps.")
print("Enter 4 for Bevrages.")
choice=int(input())
while flag==True:
    if choice == 1:
        l1 = meal.setterBrg()
        meal.ShowBrg(l1)

        want=int(input("Enter the number corrosponding to the Item You Want:: "))
        want=want-1
        qty=int(input("Enter The Quantity:: "))
        ordrs.append(meal(l1[want].name,l1[want].price,qty))
    elif choice==2:
        l3 = meal.setterDes()
        meal.ShowDes(l3)

        want = int(input("Enter the number corrosponding to the Item You Want:: "))
        want = want - 1
        qty = int(input("Enter The Quantity:: "))
        ordrs.append(meal(l1[want].name, l1[want].price, qty))
    elif choice==3:
        l4 = meal.setterSW()
        meal.ShowSW(l4)

        want = int(input("Enter the number corrosponding to the Item You Want:: "))
        want = want - 1
        qty = int(input("Enter The Quantity:: "))
        ordrs.append(meal(l1[want].name, l1[want].price, qty))
    elif choice==4:
        l2 = meal.setterBev()
        meal.ShowBev(l2)

        want = int(input("Enter the number corrosponding to the Item You Want:: "))
        want = want - 1
        qty = int(input("Enter The Quantity:: "))
        ordrs.append(meal(l1[want].name, l1[want].price, qty))
    elif choice==0:
        flag=False
        print("Thank You Very Much.")
    else :
        print("Please Enter a valid Number")
    if flag==True:
        choice=int(input("If you Want Anything More Enter The Same number Which was Shown Earlier Or Enter 0 If You Are Done:: "))

print("------------------------")
print("Your Order is as Follows:: ")
for o in ordrs:
    print(o)
meal.Show(ordrs)
