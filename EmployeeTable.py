Employees = {
  "ID" : 1,
  "Name" : "John Doe",
  "Department" : "Sales",
  "Age" : 30,
  "Email" : "john.doe@company.com"
},{
  "ID" : 2,
  "Name" : "Jane Smith",
  "Department" : "Human Resources",
  "Age" : 25,
  "Email" : "jane.smith@company.com"
},{
  "ID" : 3,
  "Name" : "Mark Johnson",
  "Department" : "IT",
  "Age" : 40,
  "Email" : "mark.johnson@company.com"
},{
  "ID" : 4,
  "Name" : "Lisa Wong",
  "Department" : "Markering",
  "Age" : 28,
  "Email" : "lisa.wong@company.com"
},{
  "ID" : 5,
  "Name" : "Paul McDonald",
  "Department" : "Finance",
  "Age" : 35,
  "Email" : "paul.mcdonald@company.com"
}
for Employee in Employees:
    print(f"ID: {Employee['ID']}, Name: {Employee['Name']}, Department: {Employee['Department']}, Age: {Employee['Age']}, Email: {Employee['Email']}")