class User: 
    def __init__(self, first_name, last_name):
         self.F_name = first_name
         self.L_name = last_name 
         print("Меня зовут", last_name, first_name)
    def sayName(self, name):
         self.F_name = name
         print("My name", name)
    def sayLast(self, last):
         self.L_name = last
         print("My last name", last)
  # Не сосвем поняла нужно ли писать еще одну функцию для одновременного вывода first_name and last_name ведь при выводе user X это и так происходит. 
  # Но лучше напишу          
    def sayLF(self, name, last):
         self.F_name = name 
         self.L_name = last   
         print("My name is", last, name)     

X = User( "Ксения ", "Гаецкая")

X.sayName("Kseniya")
X.sayLast("Gaetckaya")
X.sayLF("Xeniya", "Gaettckaya")