class Employee:
    def __init__(self, name, salary=None, hourly_wage=None, hours_worked=None, bonus=None, contracts_landed=None, commission_per_contract=None):
        self.name = name
        self.salary = salary
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked
        self.bonus = bonus
        self.contracts_landed = contracts_landed
        self.commission_per_contract = commission_per_contract

    def get_pay(self):
        pay = 0
        if self.salary:
            pay += self.salary
        if self.hourly_wage and self.hours_worked:
            pay += self.hourly_wage * self.hours_worked
        if self.bonus:
            pay += self.bonus
        if self.contracts_landed and self.commission_per_contract:
            pay += self.contracts_landed * self.commission_per_contract
        return pay

    def __str__(self):
        parts = [f"{self.name} works on a "]
        if self.salary:
            parts.append(f"monthly salary of {self.salary}")
        if self.hourly_wage and self.hours_worked:
            parts.append(f"contract of {self.hours_worked} hours at {self.hourly_wage}/hour")
        if self.bonus:
            parts.append(f"and receives a bonus commission of {self.bonus}")
        if self.contracts_landed and self.commission_per_contract:
            parts.append(f"and receives a commission for {self.contracts_landed} contract(s) at {self.commission_per_contract}/contract")
        parts.append(f". Their total pay is {self.get_pay()}.")
        return ' '.join(parts)

# Creating the employee objects
billie = Employee("Billie", salary=4000)
charlie = Employee("Charlie", hourly_wage=25, hours_worked=100)
renee = Employee("Renee", salary=3000, contracts_landed=4, commission_per_contract=200)
jan = Employee("Jan", hourly_wage=25, hours_worked=150, contracts_landed=3, commission_per_contract=220)
robbie = Employee("Robbie", salary=2000, bonus=1500)
ariel = Employee("Ariel", hourly_wage=30, hours_worked=120, bonus=600)

