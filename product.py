from baseObject import baseObject

class product(baseObject):
    def __init__(self):
        self.setup('maximus_products')
    def toList(self):
        l = []
        for row in self.data:
            s = f"{row['name']} {row['price']} {row['stock']} ({row['price']})"  
            l.append(s)
        return l
    def getByProduct(self,name): #field,value
        sql = f"Select * from `{self.tn}` where `name` = %s" 
        self.cur.execute(sql,(name))
        self.data = []
        for row in self.cur:
            self.data.append(row) 