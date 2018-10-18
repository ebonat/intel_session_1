
import sys
import config

class CalculationsClass(object):
    '''
    calculations class
    '''
    def __init__(self):
        pass
    
    def fahrenheit_to_celsius(self, fahrenheit_temperature):
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