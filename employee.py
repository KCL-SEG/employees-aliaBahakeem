
class Employee:
    def __init__(self, name, contract_type, base, hours=None, commission_type=None, contracts_landed=None, bonus=None):
        self.name = name
        self.contract_type = contract_type
        self.base = base
        self.hours = hours
        self.commission_type = commission_type
        self.contracts_landed = contracts_landed
        self.bonus = bonus

    def get_pay(self):
        if self.contract_type == "salary":
            pay = self.base
        elif self.contract_type == "hourly":
            pay = self.hours * self.base

        if self.commission_type == "contract":
            pay += self.contracts_landed * self.bonus
        elif self.commission_type == "bonus":
            pay += self.bonus

        return pay

    def __str__(self):
        description = f"{self.name} works on a "

        if self.contract_type == "salary":
            description += f"monthly salary of {self.base}. "
        elif self.contract_type == "hourly":
            description += f"contract of {self.hours} hours at {self.base}/hour. "

        if self.commission_type == "contract":
            description += f"and receives a commission for {self.contracts_landed} contract(s) at {self.bonus}/contract. "
        elif self.commission_type == "bonus":
            description += f"and receives a bonus commission of {self.bonus}. "

        description += f"Their total pay is {self.get_pay()}."
        return description

# Creating the employee objects
billie = Employee("Billie", "salary", 4000)
charlie = Employee("Charlie", "hourly", 25, hours=100)
renee = Employee("Renee", "salary", 3000, commission_type="contract", contracts_landed=4, bonus=200)
jan = Employee("Jan", "hourly", 25, hours=150, commission_type="contract", contracts_landed=3, bonus=220)
robbie = Employee("Robbie", "salary", 2000, commission_type="bonus", bonus=1500)
ariel = Employee("Ariel", "hourly", 30, hours=120, commission_type="bonus", bonus=600)
