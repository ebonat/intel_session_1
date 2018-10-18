
from base_class import Person1
from base_class import Person2

# subclass 
class Empployee1(Person1):
    '''
    for normal inheritance
    '''
    
    def __init__(self, first, last, id):
        super().__init__(first, last)
        self.idnumber = id
    
    def employee_name_id(self):
        employee_info = self.Name() + " | " +  self.idnumber
        return employee_info


class Empployee2(Person2):
    '''
    for overridden the __str__ method in Person2 class by returning the id too.
    
    Method overriding is an object-oriented programming feature that allows a 
    subclass to provide a different implementation of a method that is already 
    defined by its superclass or by one of its superclasses. The implementation 
    in the subclass overrides the implementation of the superclass by providing 
    a method with the same name, same parameters or signature, and same 
    return type as the method of the parent class. 
    '''
    
    def __init__(self, first, last, id):
        super().__init__(first, last)
        self.idnumber = id
    
    def __str__(self):
        employee_info = super().__str__() + " | " +  self.idnumber
        return employee_info
    
#     this need to be commented to implement the same below function
#     def addition_numbers(self, number_1, number_2):
#         result = number_1 + number_2
#         return result
    
# Overloading is the ability to define the same method, 
# with the same name but with a different number of 
# arguments and types. It's the ability of one function 
# to perform different tasks, depending on the number 
# of parameters or the types of the parameters.     

#     to overload in python we use the last parameter equal none and check it with the if statement
    def addition_numbers(self, number_1, number_2, number_3=None):
        if number_3 is not None:
            result = number_1 + number_2 + number_3
        else:            
            result = number_1 + number_2
        return result
    
    