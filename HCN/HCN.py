class HCNhat:
    rong = 0
    dai = 0
    ten = ""
    def __init__(self,ten,dai,rong):
        self.ten = ten
        self.dai = dai
        self.rong = rong
    def ToString(self):
        return "HCN  " + self.ten +"(" + str(self.dai) +"," + str(self.rong) +")"
    def getCV(self):
        return (int(self.rong)+ int(self.dai)) *2
    def getDT(self):
        return  (self.rong * self.dai)
    def getTen(self):
        return self.ten