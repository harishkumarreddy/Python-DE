# -*- coding: utf-8 -*-
"""
OOP/ Object Orented programming.
    1. Class
    2. Property
    3. Method
    4. Object
    
    5. Pollymorphisom
    6. Inveritation
    7. Encaptulation
    8. Interfacing
    9. Abstarction
    10. Access modifyers.
    
"""

class Student:
    # properties
    name=None
    level=None
    rno=None
    sub1=0
    sub2=0
    sub3=0
    total = 0
    result = None
    
    #methods
    def get_total(self):
        self.total = sum([self.sub1, self.sub2, self.sub3])
        return self.total
    
    def get_result(self):
        if( self.sub1 >= 35 and self.sub2 >= 35 and self.sub3 >= 35):
            tm = self.get_total()
            maxScore = 300
            percentage = (tm/maxScore)*100 
            
            if percentage <= 50:
                self.result = "C"
            elif percentage > 50 and percentage <= 60:
                self.result = "B"
            elif percentage > 60 and percentage <= 70:
                self.result = "A"
            elif percentage > 70 and percentage <= 80:
                self.result = "A+"
            elif percentage > 80:
                self.result = "A++"
        else:
            self.result = "Fail"
            
        '''if( self.sub1 < 35 or self.sub2 < 35 or self.sub3 < 35):
            self.result = "Fail"
        else:
            tm = self.get_total()
            maxScore = 300
            percentage = (tm/maxScore)*100 
            
            if percentage <= 50:
                self.result = "C"
            elif percentage > 50 and percentage <= 60:
                self.result = "B"
            elif percentage > 60 and percentage <= 70:
                self.result = "A"
            elif percentage > 70 and percentage <= 80:
                self.result = "A+"
            elif percentage > 80:
                self.result = "A++"'''
        
        return self.result
    
student1 = Student()
student1.name = "Harish"
student1.level= 1
student1.rno= 1

print(student1.name)
student1.name = "Harishkumar"
print(student1.name)


student1.sub1 = 50
student1.sub2 = 48
student1.sub3 = 35

total = student1.get_total()
print(total)

res = student1.get_result()

print(res)

























