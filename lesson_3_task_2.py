from smartphone import Smartphone

telephone1= Smartphone("Appel  ", "15 Plus    ", "+791234567")
telephone2= Smartphone("Huawei ", "Nova 12    ", "+797654321")
telephone3= Smartphone("Honor  ", "X50 GT     ", "+799876543")
telephone4= Smartphone("Appel  ", "14 Pro Max ", "+793456789")
telephone5= Smartphone("Samsung", "Galaxy 24  ", "+791029385")

catalog = [telephone1, telephone2, telephone3, telephone4, telephone5]

for x in catalog:
   print(x.brand, x.model, x.number)
