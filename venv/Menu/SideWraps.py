from Menu import lsWrp
class SW:

    def __init__(self,name,price):
        self.name=name
        self.price=price
    @classmethod
    def setterSW(cls):
        objwrp=[]
        for i, j in zip(lsWrp.keys(), lsWrp.values()):
            objwrp.append(SW(i,j))
        return objwrp

    @classmethod
    def ShowSW(cls,ls):
        count=1
        for i in ls:
            print(count,". Name = ",i.name ," price = ",i.price)
            count=count+1
