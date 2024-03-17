import sqlite3

conn = sqlite3.connect('employee.db')
conn.row_factory = sqlite3.Row
c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS employees(name TEXT, surname TEXT, age INTEGER)")
