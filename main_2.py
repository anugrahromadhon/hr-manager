import tkinter as tk
from tkinter import messagebox

class Employee:
    def __init__(self, emp_id, name, position, salary):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"ID: {self.emp_id}, Name: {self.name}, Position: {self.position}, Salary: {self.salary}"

class HRManagerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("HR Manager System")
        self.root.geometry("500x500")
        self.root.configure(bg="#f4f4f4")

        self.employees = []

        # Title Label
        title_label = tk.Label(root, text="HR Manager System", font=("Helvetica", 16, "bold"), bg="#4CAF50", fg="white", pady=10)
        title_label.pack(fill=tk.X)

        # Input Frame
        input_frame = tk.Frame(root, bg="#f4f4f4")
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Employee ID:", bg="#f4f4f4").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        self.emp_id_entry = tk.Entry(input_frame)
        self.emp_id_entry.grid(row=0, column=1, pady=5)

        tk.Label(input_frame, text="Name:", bg="#f4f4f4").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
        self.name_entry = tk.Entry(input_frame)
        self.name_entry.grid(row=1, column=1, pady=5)

        tk.Label(input_frame, text="Position:", bg="#f4f4f4").grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
        self.position_entry = tk.Entry(input_frame)
        self.position_entry.grid(row=2, column=1, pady=5)

        tk.Label(input_frame, text="Salary:", bg="#f4f4f4").grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
        self.salary_entry = tk.Entry(input_frame)
        self.salary_entry.grid(row=3, column=1, pady=5)

        # Button Frame
        button_frame = tk.Frame(root, bg="#f4f4f4")
        button_frame.pack(pady=10)

        add_button = tk.Button(button_frame, text="Add Employee", bg="#4CAF50", fg="white", command=self.add_employee)
        add_button.grid(row=0, column=0, padx=10)

        view_button = tk.Button(button_frame, text="View Employees", bg="#2196F3", fg="white", command=self.view_employees)
        view_button.grid(row=0, column=1, padx=10)

        search_button = tk.Button(button_frame, text="Search Employee", bg="#FF9800", fg="white", command=self.search_employee)
        search_button.grid(row=0, column=2, padx=10)

        remove_button = tk.Button(button_frame, text="Remove Employee", bg="#F44336", fg="white", command=self.remove_employee)
        remove_button.grid(row=0, column=3, padx=10)

        # Listbox
        self.listbox = tk.Listbox(root, width=60, height=15)
        self.listbox.pack(pady=10)

    def add_employee(self):
        emp_id = self.emp_id_entry.get()
        name = self.name_entry.get()
        position = self.position_entry.get()
        salary = self.salary_entry.get()

        if emp_id and name and position and salary:
            try:
                salary = float(salary)
                new_employee = Employee(emp_id, name, position, salary)
                self.employees.append(new_employee)
                messagebox.showinfo("Success", f"Employee {name} added successfully!")
                self.clear_entries()
            except ValueError:
                messagebox.showerror("Error", "Salary must be a number.")
        else:
            messagebox.showerror("Error", "All fields are required.")

    def remove_employee(self):
        emp_id = self.emp_id_entry.get()
        if emp_id:
            for employee in self.employees:
                if employee.emp_id == emp_id:
                    self.employees.remove(employee)
                    messagebox.showinfo("Success", f"Employee {employee.name} removed successfully!")
                    self.clear_entries()
                    return
            messagebox.showerror("Error", "Employee not found.")
        else:
            messagebox.showerror("Error", "Employee ID is required.")

    def view_employees(self):
        self.listbox.delete(0, tk.END)
        if not self.employees:
            self.listbox.insert(tk.END, "No employees found.")
        else:
            for employee in self.employees:
                self.listbox.insert(tk.END, str(employee))

    def search_employee(self):
        emp_id = self.emp_id_entry.get()
        if emp_id:
            self.listbox.delete(0, tk.END)
            for employee in self.employees:
                if employee.emp_id == emp_id:
                    self.listbox.insert(tk.END, str(employee))
                    return
            self.listbox.insert(tk.END, "Employee not found.")
        else:
            messagebox.showerror("Error", "Employee ID is required.")

    def clear_entries(self):
        self.emp_id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.position_entry.delete(0, tk.END)
        self.salary_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = HRManagerGUI(root)
    root.mainloop()
