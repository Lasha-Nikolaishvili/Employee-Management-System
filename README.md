# Employee Management System

This Python script is designed to manage an employee database using SQLite. It provides functionality to create a table for employee information, insert sample employee data into the table, perform various operations such as creating, retrieving, updating and deleting employees.

## Features

- **Creating Table**: The script creates a table named `employees` with columns for employee name, surname and age.
  
- **Inserting Employees**: Sample employee data is provided in the `main.py` file. The script inserts this data into the `employees` table using the `create_many()` class method.

- **Selecting Employees**: The `get_list()` class method retrieves employees from the `employees` table based on provided parameters and returns them as a list of Employee instances.

- **Updating Employees**: The `update_many()` class method updates employees from the `employees` table based on provided parameters and returns the number of affected rows.

- **Deleting Employees**: The `delete_many()` class method deletes employees from the `employees` table based on provided parameters and returns the number of affected rows.

- **Other Features**: There are other methods whose usage guide is provided in the `main.py` file.
 
## Usage

To use this script:

1. Make sure you have Python installed on your system.

2. Run the script `main.py`. This will execute the main function, which creates and displays example users. You can use the user guide to experiment with the database.

## Requirements

- Currently, the project doesn't have any requirements besides Python.

## Notes

- The script assumes that an SQLite database file named `employee.db` exists in the current directory. If not, it will be created automatically.