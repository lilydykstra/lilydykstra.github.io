//problem 1
const employeeDetails = {
    "employees" : [
    {
        "Name" : "Sam",
        "Department": "Tech",
        "Designation": "Manager",
        "Salary": "40000",
        "Raise Eligible": "True"
    },
    {    
        "Name" : "Mary",
        "Department": "Finance",
        "Designation": "Trainee",
        "Salary": "18500",
        "Raise Eligible": "True"
    },
    {    
        "Name" : "Bill",
        "Department": "HR",
        "Designation": "Executive",
        "Salary": "21200",
        "Raise Eligible": "False"}
    ]
};

console.log("Problem #1")
console.log(employeeDetails)

//problem 2
const companyDetails = {
    "company" : [
    {
        "Name" : "Tech Stars",
        "Website": "www.techstars.site",
        "Employees": employeeDetails
    }
    ]
};
console.log("Problem #2")
console.log(companyDetails)

//problem 3
employeeDetails.employees[3]= {    
        "Name" : "Anna",
        "Department": "Tech",
        "Designation": "Executive",
        "Salary": "25600",
        "Raise Eligible": "False"}


console.log("Problem #3")
console.log(employeeDetails)

//problem 4
totalSalary = 0
for (employees of employeeDetails.employees){
        totalSalary += parseInt(employees.Salary);
}
console.log("Problem #4")
console.log('Total Salary: $',totalSalary)

//problem 5
for (employees of employeeDetails.employees){
    if (employees["Raise Eligible"] === "True"){
        employees.Salary = employees.Salary*1.1
        employees["Raise Eligible"] = "False"
    }
}
console.log("Problem #5")
console.log(employeeDetails)

//problem 6
const workingfromhome = ["Anna","Sam"]
for ( employee of employeeDetails.employees){
    if (workingfromhome.includes(employee.Name)){
        employee.wfh = "True";
    }    
    else{
        employee.wfh = "False";
    }
}
console.log("Problem #6")
console.log(employeeDetails)