import numpy as nр
dtype = [('name', 'U20'), ('height', 'f4'), ('class', 'U10')]
students = np.array([('Toan', 1.65, 'A'),
                     ('Tuong', 1.78, 'B'),
                     ('Viet', 1.72, 'C'),
                     ('Tuan', 1.58, 'B')],
                    dtype=dtype)
sorted_students = np.sort(students, order='height')

print(sorted_students)
