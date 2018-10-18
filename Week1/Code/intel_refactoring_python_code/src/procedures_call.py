
import procedures
# from procedures import *

from calculations import CalculationsClass

def function_1(fDegrees): 
    Celsius = procedures.Celsius(fDegrees)
    return Celsius    

def function_2(fahrenheit_temperature):
    exception_message, celsius_temperature = procedures.fahrenheit_to_celsius(fahrenheit_temperature)
    return exception_message, celsius_temperature

def function_3(fahrenheit_temperature):
    calculations = CalculationsClass()
    exception_message, celsius_temperature = calculations.fahrenheit_to_celsius(fahrenheit_temperature)
    return exception_message, celsius_temperature

def main():
#     bad python code
    fDegrees = 65
    Celsius = function_1(fDegrees)
    print("The temperature is " +  str(Celsius) + " degrees C.")
    
#     good python code
    fahrenheit_temperature = 65
    exception_message, celsius_temperature = function_2(fahrenheit_temperature)    
    if celsius_temperature is not None:
        print("The temperature is {} degrees C.".format(str(celsius_temperature)))
    else:
        print("An error occurred. {}".format(exception_message))
                
#     excellent python code
    fahrenheit_temperature = 65
    exception_message, celsius_temperature = function_3(fahrenheit_temperature)    
    if celsius_temperature is not None:
        print("The temperature is {} degrees C.".format(str(celsius_temperature)))
    else:
        print("An error occurred. {}".format(exception_message))
        

if __name__ == '__main__':
    main()