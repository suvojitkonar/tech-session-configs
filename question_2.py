def convert_fahrenheit_to_celsius(temperature):
    return ((temperature - 32)*5)/9
    
temperature = input('Enter temperature in degrees fahrenheit: ')
converted_temperature = convert_fahrenheit_to_celsius(temperature)
print('The converted temperature in degree celsius is: ', converted_temperature)
