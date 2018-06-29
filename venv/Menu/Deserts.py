from Menu import lsDes
class Des:

    def __init__(self,name,price):
        self.name=name
        self.price=price
    @classmethod
    def setterDes(cls):
        objdes=[]
        for i, j in zip(lsDes.keys(), lsDes.values()):
            objdes.append(Des(i,j))
        return objdes

    @classmethod
    def ShowDes(cls,ls):
        count=1
        for i in ls:
            print(count,". Name = ",i.name ," price = ",i.price)
            count=count+1
