def convert_temperature(celsius):
    """
    -------------------------------------------------------
    Converts a temperature in Celsius to Fahrenheit and Kelvin.
    The conversion formulas are given below:
        Celsius to Fahrenheit: F = (C * 9/5) + 32  
        Celsius to Kelvin: K = C + 273.15
    Use: fahrenheit, kelvin = convert_temperature(celsius)
    -------------------------------------------------------
    Parameters:
        celsius - temperature in Celsius (float)
    Returns:
        fahrenheit  - temperature in Fahrenheit (float)
        kelvin - temperature in Kelvin (float)
    -------------------------------------------------------
    """
    # Your code here
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
    
    
    return fahrenheit, kelvin