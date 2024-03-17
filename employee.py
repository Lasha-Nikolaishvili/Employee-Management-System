from db import c


def construct_query(query_type, name, surname, age, pid):
    sql_query = ["SELECT *, rowid FROM employees WHERE 1=1"]
    params = []

    if query_type == "delete":
        sql_query = ["DELETE FROM employees WHERE 1=1"]

    if name is not None:
        sql_query.append("AND name = ?")
        params.append(name)
    if surname is not None:
        sql_query.append("AND surname = ?")
        params.append(surname)
    if age is not None:
        sql_query.append("AND age = ?")
        params.append(age)
    if pid is not None:
        sql_query.append("AND pid = ?")
        params.append(pid)

    return ' '.join(sql_query), params


class Employee(object):
    def __init__(self, name, surname, age):
        self.pid = None
        self.name = name
        self.surname = surname
        self.age = age

    def __repr__(self):
        return f"Employee(name={self.name}, surname={self.surname}, age={self.age}, pid={self.pid})"

    def __eq__(self, other):
        if isinstance(other, Employee):
            return other.age == self.age
        return False

    def __lt__(self, other):
        if isinstance(other, Employee):
            return self.age < other.age
        return False

    def __ge__(self, other):
        if isinstance(other, Employee):
            return not self.__lt__(other)
        return False

    def __le__(self, other):
        if isinstance(other, Employee):
            return self.age <= other.age
        return False

    def __gt__(self, other):
        if isinstance(other, Employee):
            return not self.__le__(other)
        return False

    @classmethod
    def get(cls, pid):
        result = c.execute("SELECT *, rowid FROM employees WHERE rowid = ?", (pid,))
        row = result.fetchone()

        if row is None:
            return None

        employee = Employee(row["name"], row["surname"], row["age"])
        employee.pid = row["rowid"]

        return employee

    @classmethod
    def get_list(cls, name=None, surname=None, age=None, pid=None):
        sql_query, params = construct_query("select", name, surname, age, pid)

        result = c.execute(sql_query, params)
        rows = result.fetchall()

        if rows is None:
            return None

        employees = []
        for row in rows:
            employee = Employee(name=row["name"], surname=row["surname"], age=row["age"])
            employee.pid = row["rowid"]

            employees.append(employee)

        return employees

    def update(self):
        c.execute("UPDATE employees SET name = ?, surname = ?, age = ? WHERE rowid = ?",
                  (self.name, self.surname, self.age, self.pid))

        return self

    def create(self):
        c.execute("INSERT INTO employees (name, surname, age) VALUES (?, ?, ?)",
                  (self.name, self.surname, self.age))
        self.pid = c.lastrowid + 1

        return self

    @classmethod
    def create_many(cls, employee_params_array):
        employees = []
        employee_pid_counter = c.lastrowid + 1

        for employee_params in employee_params_array:
            employee = Employee(employee_params[0], employee_params[1], employee_params[2])
            employee.pid = employee_pid_counter
            employee_pid_counter += 1

            employees.append(employee)

        c.executemany("INSERT INTO employees (name, surname, age) VALUES (?, ?, ?)",
                      employee_params_array)

        return employees

    def save(self):
        if self.pid is not None:
            self.update()
        else:
            self.create()

        return self

    def delete(self):
        c.execute("DELETE FROM employees WHERE rowid = ?", (self.pid,))

        return self

    @classmethod
    def delete_many(cls, name=None, surname=None, age=None, pid=None):
        sql_query, params = construct_query("delete", name, surname, age, pid)
        result = c.execute(sql_query, params)

        return f"Deleted {result.rowcount} row(s)."

    @classmethod
    def update_many(cls, update_data, condition):
        sql_query = f"UPDATE employees SET {', '.join(f'{key} = ?' for key in update_data.keys())}"
        if condition:
            sql_query += " WHERE " + condition

        params = list(update_data.values())
        result = c.execute(sql_query, params)

        return f"Updated {result.rowcount} row(s)."
