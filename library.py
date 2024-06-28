class Person:
    def init(self, fam, name, otchestvo, numdepartment, workdays, salary):
        self.fam = fam
        self.name = name
        self.otchestvo = otchestvo
        self.numdepartment = numdepartment
        self.workdays = workdays
        self.salary = salary


def get_person_data(self):
    return [self.fam, self.name, self.otchestvo, self.num_department, self.work_days, self.salary]

class Group:
    def init(self):
        self.employees = {}
        self.count = 0


def __str__(self):
    s = ''
    for x in range(len(self.employees)):
        if x in self.employees:
            s += f'employee {x+1}:\\n'
            s += str(self.employees[x].get_person_data())
            s += '\\n'
    return s

def read_data_from_file(self, filename):
    self.employees = {}
    x = 0
    with open(filename, "r") as file:
        for line in file:
            if line[-1] == '\\n':
                line = line[:-1]
            parts = line.strip().split(" ")
            self.employees[x] = Person(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5])
            x += 1
            self.count += 1

def write_data_to_file(self, department_number, filename):
    with open(filename, "w") as file:
        for x in range(len(self.employees)):
            if x in self.employees and self.employees[x].num_department == department_number:
                file.write(f"{self.employees[x].fam} {self.employees[x].name} {self.employees[x].otchestvo} {self.employees[x].num_department} {self.employees[x].work_days} {self.employees[x].salary}\\n")

def sort_and_filter_by_salary(self, department_number, salary_threshold):
    filtered_list = [self.employees[x] for x in range(len(self.employees)) if x in self.employees and self.employees[x].num_department == department_number and self.employees[x].salary > salary_threshold]
    sorted_list = sorted(filtered_list, key=lambda x: x.salary)
    return sorted_list

def linear_search(self, department_number, salary_threshold):
    filtered_list = [self.employees[x] for x in range(len(self.employees)) if x in self.employees and self.employees[x].num_department == department_number and self.employees[x].salary > salary_threshold]
    return filtered_list

def find_min_work_days(self):
    min_work_days = min([self.employees[x].work_days for x in range(len(self.employees)) if x in self.employees])
    employees_with_min_work_days = [self.employees[x] for x in range(len(self.employees)) if x in self.employees and self.employees[x].work_days == min_work_days]
    return employees_with_min_work_days

def average_salary_in_department(self, department_number):
    total_salary = sum([self.employees[x].salary for x in range(len(self.employees)) if x in self.employees and self.employees[x].num_department == department_number])
    num_employees = len([self.employees[x] for x in range(len(self.employees)) if x in self.employees and self.employees[x].num_department == department_number])
    if num_employees == 0:
        return 0
    return total_salary / num_employees

def set_salary(self, fam, new_salary):
    for x in range(len(self.employees)):
        if x in self.employees and self.employees[x].fam == fam:
            self.employees[x].salary = new_salary

def add_employee(self, fam, name, otchestvo, num_department, work_days, salary):
    self.employees[self.count] = Person(fam, name, otchestvo, num_department, work_days, salary)
    self.count += 1

def remove_employee(self, fam):
    for x in range(len(self.employees)):
        if x in self.employees and self.employees[x].fam == fam:
            del self.employees[x]
            break

def update_employee_info(self, fam, new_name, new_otchestvo, new_num_department, new_work_days, new_salary):
    for x in range(len(self.employees)):
        if x in self.employees and self.employees[x].fam == fam:
            self.employees[x].name = new_name
            self.employees[x].otchestvo = new_otchestvo
            self.employees[x].num_department = new_num_department
            self.employees[x].work_days = new_work_days
            self.employees[x].salary = new_salary

def total_num_employees(self):
    return len(self.employees)
