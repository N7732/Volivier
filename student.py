class Student:
    def __init__(self,name,Reg_number,Mathematics,Physics):
        self.name=name
        self.Reg_number=Reg_number
        self.Mathematics=Mathematics
        self.Physics=Physics
   
    def sum(self):
        a=self.Mathematics +self.Physics
        return a
obj1=Student("Olivier",224008132,30,70)
print(obj1.sum())