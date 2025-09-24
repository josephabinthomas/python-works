class person:
        def __init__(self, name, age):
          self.name = name
          self.age = age
        def show_details(self):
          print("Name:", self.name)
          print("Age:", self.age)
class employee(person):
        def __init__(self, name, age, employee_id):
          super().__init__(name, age)
          self.employee_id = employee_id
        def show_details(self):
          super().show_details()
          print("Employee ID:", self.employee_id)
class PartTime(person): 
        def __init__(self, name, age, working_hours):
          super().__init__(name, age)
          self.working_hours = working_hours
        def show_details(self):
          super().show_details()
          print("Working Hours:", self.working_hours)
class Consultant(employee, PartTime):
        def __init__(self, name, age, employee_id, working_hours, project_name):
          employee.__init__(self, name, age, employee_id)
          PartTime.__init__(self, name, age, working_hours)
          self.project_name = project_name
        def show_details(self):
          super().show_details()
          print("Working Hours:", self.working_hours)
          print("Project Name:", self.project_name)
p = person("vishnu", 30)
e = employee("ashik", 40, "E101")
pt = PartTime("samiya", 25, 20.5)
c = Consultant("salman", 35, "C202", 10.0, "security Project")

print("\nPerson:")
p.show_details()

print("\nEmployee:")
e.show_details()

print("\nPart-Time:")
pt.show_details()

print("\nConsultant:")
c.show_details()

