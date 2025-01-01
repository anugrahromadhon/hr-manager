# HR Manager System

## Overview
HR Manager System is a simple and intuitive application designed for small businesses to manage their employee data efficiently. The system provides both a command-line interface (CLI) and a graphical user interface (GUI) built with Tkinter. Users can add, view, search, and remove employee records through these interfaces, offering flexibility based on user preference.

## Features
- **Add Employee**: Register a new employee with their ID, name, position, and salary.
- **Remove Employee**: Delete employee records based on their ID.
- **View Employees**: Display a list of all registered employees.
- **Search Employee**: Search for employee details by their ID.

### CLI Version
- Fully text-based for use in terminals.
- Lightweight and fast.
- Easy to integrate into server-side automation scripts.

### GUI Version
- Professional color scheme for intuitive navigation:
  - Green (#4CAF50): Add Employee.
  - Blue (#2196F3): View Employees.
  - Orange (#FF9800): Search Employee.
  - Red (#F44336): Remove Employee.
- Responsive design to display employee data in a clean and organized list.
- Error handling with popup messages for invalid inputs or missing fields.

## Technology Stack
- **Programming Language**: Python
- **Libraries**: Tkinter (for GUI)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/anugrahromadhon/hr-manager.git
   ```
2. Navigate to the project directory:
   ```bash
   cd hr-manager
   ```
3. Ensure Python 3.x is installed on your system.

## Usage
### Running the CLI Version
1. Navigate to the project directory.
2. Run the CLI script:
   ```bash
   python main.py
   ```
3. Follow the prompts to manage employee records.

### Running the GUI Version
1. Navigate to the project directory.
2. Run the GUI script:
   ```bash
   python main_2.py
   ```
3. Use the graphical interface to manage employee records:
   - Fill out the input fields and click **Add Employee** to register a new employee.
   - Click **View Employees** to display all registered employees.
   - Enter an ID and click **Search Employee** to find specific employee details.
   - Enter an ID and click **Remove Employee** to delete an employee.

## Folder Structure
```
hr-manager/
├── main.py           # CLI version script
├── main_2.py         # GUI version script
├── README.md         # Documentation
└── employees_data/   # (Optional) Folder to store future enhancements
```

## Future Enhancements
- Export employee data to a CSV file.
- Add a database for persistent storage.
- Support for additional employee attributes (e.g., department, hire date).

## License
This project is open-source and available under the [MIT License](LICENSE).

## Contributing
Contributions are welcome! Feel free to fork the repository, create a branch, and submit a pull request.

