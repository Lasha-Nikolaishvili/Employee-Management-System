"""
----- User Guide -----
* To select a single employee from a table
    Employee.get(rowid)

* To add a single employee to a table
    employee = Employee("John", "Doe", 40)
    employee.create()

* To update a single employee from a table
    employee = Employee("John", "Doe", 40)
    employee.name = "Jane"
    employee.update()

* To add or update a single employee to a table
    employee = Employee("John", "Doe", 40)
    employee.save()

* To delete a single employee from a table
    employee = Employee("John", "Doe", 40)
    employee.delete()

* To get an employee list based on different parameters
    Employee.get_list(name='name', surname="...")

* To update employees based on different parameters
    Employee.update_many(name='name', surname="...")

* To delete employees based on different parameters
    Employee.delete_many(name='name', surname="...")

* To update many employees based on a condition
    update_data = {'name': 'name', 'surname': 'surname'}
    condition = "age = 20"  # Optional condition
    Employee.update_many(update_data, condition)

* To create many employee objects and add them to the database
    employees = Employee.create_many(
        [
            ("Bruce", "Wayne", 35),
            ("Clark", "Kent", 32)
        ]
    )
"""

from employee import Employee
from db import conn


# Creating example users:
employees = Employee.create_many(
    [
        ("Barry", "Allen", 29),
        ("Bruce", "Wayne", 30),
        ("Clark", "Kent", 30),
        ("Steve", "Rogers", 101),
        ("Peter", "Parker", 16),
        ("Natasha", "Romanoff", 27),
        ("Tony", "Stark", 37),
        ("Thor", "Odinson", 35),
        ("Loki", "Odinson", 38),
    ]
)

# Displaying users:
rows = Employee.get_list()
for row in rows:
    print(row)

conn.commit()
conn.close()
