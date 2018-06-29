from Menu import lsBrg
class Brg:

    def __init__(self,name,price):
        self.name=name
        self.price=price
    @classmethod
    def setterBrg(cls):
        objbrg=[]
        for i, j in zip(lsBrg.keys(), lsBrg.values()):
            objbrg.append(Brg(i,j))
        return objbrg

    @classmethod
    def ShowBrg(cls,ls):
        count=1
        for i in ls:
            print(count,". Name = ",i.name ," price = ",i.price)
            count=count+1


#l1=FoodItem.setter()
#FoodItem.ShowBrg(l1)