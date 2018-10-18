
from derived_class import Empployee1
from derived_class import Empployee2

def main():
#     for normal inheritance
    employee1 = Empployee1("John", "Smith", "100")        
    employee_info1 = employee1.employee_name_id()    
    print(employee_info1)
    
#     for overridden the __str__ method
    employee2 = Empployee2("John", "Smith", "100")        
    employee_info2 = employee2.__str__()
    print(employee_info2)
    
if __name__ == '__main__':
    main()