
class Employee:
    def __init__(self, name: str, hours_worked: float, hourly_rate: float):
        self.name = name
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_pay(self) -> float:
        regular_hours = min(self.hours_worked, 40)
        overtime_hours = max(self.hours_worked - 40, 0)
        
        regular_pay = regular_hours * self.hourly_rate
        
        overtime_pay = overtime_hours * self.hourly_rate * 1.5
        
        total_pay = regular_pay + overtime_pay
        
        return total_pay

class Manager(Employee):
    def __init__(self, name: str, hours_worked: float, hourly_rate: float, bonus: float):
        super().__init__(name, hours_worked, hourly_rate)
        self.bonus = bonus

    def calculate_pay(self) -> float:
        base_pay = super().calculate_pay()
        
        total_pay = base_pay + self.bonus
        
        return total_pay

if __name__ == "__main__":
    employee = Employee("John Doe", 45, 20)
    employee_pay = employee.calculate_pay()
    print(f"Total pay for {employee.name} (Employee): ${employee_pay:.2f}")
    
    manager = Manager("Jane Smith", 50, 30, 500)
    manager_pay = manager.calculate_pay()
    print(f"Total pay for {manager.name} (Manager): ${manager_pay:.2f}")
