from Menu import lsBev
class Bev:

    def __init__(self,name,price):
        self.name=name
        self.price=price
    @classmethod
    def setterBev(cls):
        objbev=[]
        for i, j in zip(lsBev.keys(), lsBev.values()):
            objbev.append(Bev(i,j))
        return objbev

    @classmethod
    def ShowBev(cls,ls):
        count=1
        for i in ls:
            print(count,". Name = ",i.name ," price = ",i.price)
            count=count+1

