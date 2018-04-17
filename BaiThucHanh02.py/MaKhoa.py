class SinhVien1:
	
	def __init__(self,MaKhoa,TenKhoa):
	
		self.MaKhoaV=MaKhoa
	
		self.TenKhoa=TrenKhoa
	
	def getMaKhoa(self):
		
		return self.MaKhoa
	
	def setMaKhoa(self,MaKhoa):
	
		return self.MaKhoa=MaKhoa

	def getTenKhoa(self):
	
		return self.TenKhoa
	
	def setTenKhoa(self,MaKhoa):
		
		eturn self.TenKhoa=TenKhoa
	
	def ToString(self):
	
	print self.MaKhoa+ "----" ,self.TenKhoa
