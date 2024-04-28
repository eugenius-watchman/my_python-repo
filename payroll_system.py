from abc import ABC, abstractmethod


class Employee(ABC):

    def __init__(self, first, last, ssn):
        self.__first_name = first
        self.__last_name = last
        self.__ssn = ssn

    def setFirstName(self, f_name):
        self.__first_name = f_name

    def getFirstName(self):
        return self.__first_name

    def setLastName(self, l_name):
        self.__last_name = l_name

    def getLastName(self):
        return self.__last_name

    def setSSN(self, ssn):
        self.__ssn = ssn

    def getSSN(self):
        return self.__ssn

    # check if value entered by user is positive or not
    def checkPositive(self, value):
        if value < 0:
            msg = "Attribute value {} must be positive".format(value)
            raise ValueError(msg)
        else:
            return value

    # str function
    def __str__(self):
        return "{} {} Social Security Number: {}".format(self.getFirstName(), self.getLastName(), self.getSSN())

    @abstractmethod
    def earning(self):
        pass


# salaried Employee Class ... child of Employee Class
class SalariedEmployee(Employee, ABC):

    def __init__(self, first, last, ssn, salary):
        # call the initializer function or constructor of the abstract class
        super().__init__(first, last, ssn)
        # initialize the weekly salary
        self.__weekly_salary = self.checkPositive(salary)

    def setWeeklySalary(self, salary):
        self.__weekly_salary = self.checkPositive(salary)

    def getWeeklySalary(self):
        return self.__weekly_salary

    # override the abstract function earning in the employee class
    def earning(self):
        return self.getWeeklySalary()

    def __str__(self):
        return "Salaried Employee: {} \n{} {:.2f}".format(super().__str__(), "Weekly Salary", self.getWeeklySalary())


# hourly employee class
class HourlyEmployee(Employee, ABC):
    def __init__(self, first, last, ssn, hourly_wage, hours_worked):
        # call the initializer function of the parent class
        super().__init__(first, last, ssn)

        # user validations while we initialize some variables
        self.__wage = self.setWage(hourly_wage)
        self.__hours = self.setHours(hours_worked)

    def setWage(self, hourly_wage):
        self.__wage = self.checkPositive(hourly_wage)
        return self.__wage

    def getWage(self):
        return self.__wage

    def setHours(self, hours_worked):

        if 0.0 <= hours_worked <= 168.0:
            self.__hours = hours_worked
            return self.__hours
        else:
            raise ValueError("Hourly wage must be >= 0.0")

    def getHours(self):
        return self.__hours

    # override the earning method
    def earning(self):
        if self.getHours() <= 40:
            return self.getWage() * self.getHours()
        else:
            return 40 * self.getWage() + (self.getHours() - 40) * self.getWage() * 1.5

    # override str function of employee class
    def __str__(self):
        return "Hourly Employee: {} \n {}: {:.2f} {}: {:.2f}".format(super().__str__(),"Hourly Wage", self.getWage(),
                                                                     "Hours Worked", self.getHours())


# commission employee class
class CommissionEmployee(Employee, ABC):
    def __init__(self, first, last, ssn, gross_sales, rate):
        super().__init__(first, last, ssn)
        self.__commission_rate = self.setCommissionRate(rate)
        self.__gross_sales = self.setGrossSales(gross_sales)

    # user validations for setter functions
    def setCommissionRate(self, rate):
        if 0.0 < rate < 1.0:
            self.__commission_rate = rate
            return self.__commission_rate
        else:
            raise ValueError("Commission Rate must be between 0.0 and 1.0")

    def getCommissionRate(self):
        return self.__commission_rate

    def setGrossSales(self, sales):
        self.__gross_sales = self.checkPositive(sales)
        return self.__gross_sales

    def getGrossSales(self):
        return self.__gross_sales

    # override the earning method
    def earning(self):
        return self.getCommissionRate() * self.getGrossSales()

    # override str function of employee class
    def __str__(self):
        return "Commission Employee: {} \n {}: {:.2f} {}: {:.2f}".format(super().__str__(),
                                                                         "Gross Sales: ", self.getGrossSales(),
                                                                         "Commission Rate: ", self.getCommissionRate())


# main program
salaryEmp = SalariedEmployee("Eugene", "Darrah", "111-11-1111", 900.00)
hourlyEmp = HourlyEmployee("Mbroba", "Sandy", "222-22-2222", 20.75, 40)
commissionEmp = CommissionEmployee("Elexina", "Princella", "333-33-3333", 10000, .06)

print("\nsalaryEmp is an Employee's object:", isinstance(salaryEmp, Employee))
print("hourlyEmp is an Employee's object:", isinstance(hourlyEmp, Employee))
print("CommissionEmp is subclass of an Employee: ", issubclass(CommissionEmployee, Employee))

print()
print("Employees processed individually:\n")
print(salaryEmp, "earned", salaryEmp.earning())
print(hourlyEmp, "earned", hourlyEmp.earning())
print(commissionEmp, "earned", commissionEmp.earning())

# create a list of employees
employees = [salaryEmp, hourlyEmp, commissionEmp]

for employee in employees:
    print(employee.earning())