class PhepToan:
    sothunhat =0
    sothuhai=0
    def __init__(self,sothunhat,sothuhai):
        self.sothuhai = sothuhai
        self.sothunhat = sothunhat
    def getso1(self):
        return self.sothunhat
    def getSo2(self):
        return self.sothuhai
    def PhepCong(self):
        return int(self.sothuhai) + int(self.sothunhat)
    def PhepTru(self):
        return int(self.sothunhat)-int(self.sothuhai)
    def PhepNhan(self):
        return int(self.sothuhai) * int(self.sothunhat)
    def PhepChia(self):
        return  int(self.sothunhat) / int(self.sothuhai)
    def ToString(self):
        return "Thuc Hien Phep Toan voi 2 so A B :"