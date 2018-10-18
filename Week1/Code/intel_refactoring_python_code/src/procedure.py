
import sys
import config

# bad python function 
def Celsius(fDegrees):
    _Celsius = (fDegrees - 32) * 5 / 9
    return _Celsius;

# good python function
def fahrenheit_to_celsius(fahrenheit_temperature):
    '''
    convert fahrenheit temperature to celsius
    :param fahrenheit_temperature: temperature in fahrenheit
    :return 
    1. exception_message: string exception message 
    2. celsius_temperature: temperature in celsius
    '''
    celsius_temperature = None
    exception_message = None
    try:
        celsius_temperature = (fahrenheit_temperature - config.NUMBER_32) * config.NUMBER_5_DIVIDED_9
    except:
        exception_message = sys.exc_info()[1]
    return exception_message, celsius_temperature
    