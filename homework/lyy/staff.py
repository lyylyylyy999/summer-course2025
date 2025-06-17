class Staff:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def print_info(self):
        print(f"{self.name}(id为{self.id})")

class FullTimeEmployee(Staff):
    def __init__(self,name,id,monthly_salary):
        super().__init__(name,id)
        self.monthly_salary = monthly_salary
        
    def calculate_monthly_pay(self):
        return self.monthly_salary
    
class PartTimeEmployee(Staff):
    def __init__(self,name,id,daily_salary,work_days):
        super().__init__(name,id)
        self.daily_salary = daily_salary
        self.work_days = work_days
        
    def calculate_monthly_pay(self):
        return self.daily_salary * self.work_days
    
li = FullTimeEmployee("lyy","202140210221",10000)
xiong = PartTimeEmployee("xsz","202140210224",300,20)
li.print_info()
xiong.print_info()
print(f"{li.name}的月薪为{li.calculate_monthly_pay()}")
print(f"{xiong.name}的月薪为{xiong.calculate_monthly_pay()}")