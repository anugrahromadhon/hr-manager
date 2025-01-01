class Employee:
    def __init__(self, emp_id, name, position, salary):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"ID: {self.emp_id}, Name: {self.name}, Position: {self.position}, Salary: {self.salary}"

class HRManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp_id, name, position, salary):
        new_employee = Employee(emp_id, name, position, salary)
        self.employees.append(new_employee)
        print(f"Employee {name} added successfully!")

    def remove_employee(self, emp_id):
        for employee in self.employees:
            if employee.emp_id == emp_id:
                self.employees.remove(employee)
                print(f"Employee {employee.name} removed successfully!")
                return
        print("Employee not found.")

    def view_all_employees(self):
        if not self.employees:
            print("No employees found.")
        else:
            print("Employee List:")
            for employee in self.employees:
                print(employee)

    def search_employee(self, emp_id):
        for employee in self.employees:
            if employee.emp_id == emp_id:
                print("Employee Found:")
                print(employee)
                return
        print("Employee not found.")

# Main Program
if __name__ == "__main__":
    hr_manager = HRManager()

    while True:
        print("\nHR Manager System")
        print("1. Add Employee")
        print("2. Remove Employee")
        print("3. View All Employees")
        print("4. Search Employee")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Employee Name: ")
            position = input("Enter Employee Position: ")
            salary = float(input("Enter Employee Salary: "))
            hr_manager.add_employee(emp_id, name, position, salary)

        elif choice == "2":
            emp_id = input("Enter Employee ID to Remove: ")
            hr_manager.remove_employee(emp_id)

        elif choice == "3":
            hr_manager.view_all_employees()

        elif choice == "4":
            emp_id = input("Enter Employee ID to Search: ")
            hr_manager.search_employee(emp_id)

        elif choice == "5":
            print("Exiting HR Manager System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
