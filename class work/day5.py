python={"manu","akash","akhil","vishnu"}
datascience={"manu","joseph","abin","ashik"}
python.add("james")
datascience.remove("manu")
print(python)
print(datascience)
print(python & datascience)
print(python - datascience)
print(python | datascience)
course={
    "python":(len(python)),
    "datascience":(len(datascience))  
}
print(course)
for name, count in course.items():
    print(f"Course: {name}, Students: {count}")
    
double = {name: count * 2 for name, count in course.items()}
print(double)