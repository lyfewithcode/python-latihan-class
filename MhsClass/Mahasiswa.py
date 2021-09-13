# nim, nama, telepon, semester

class Mahasiswa:
   def __init__(self, nim, nm, tlp, smt):
      self.nim = nim
      self.nama = nm
      self.telepon = tlp
      self.semester = smt

   def getNim(self):
      print(self.nim)

   def getNama(self):
      print(self.nama)

   def getTelepon(self):
      print(self.telepon)

   def getSemester(self):
      print(self.semester)