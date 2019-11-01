#!/usr/bin/env python3


class Company():
    def __init__(self,name,income,employees):
        self.name = name
        self.income = income
        self.employees = employees

    def information(self):
        return self.name,self.income,self.employees

myCompany = Company("Wookie", 3.5, 2 )

print(myCompany.information())
