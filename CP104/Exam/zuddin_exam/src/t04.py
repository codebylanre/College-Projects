from t04_functions import convert_temperature

CASES = (-5, 36, 180, -273.15, -40)

for case in CASES:
    print(f'convert_temperature({case}) → {convert_temperature(case)}')
    print()

print("my test")
celsius = -5
fahrenheit, kelvin = convert_temperature(celsius)
print(f"{fahrenheit:.1f} fahrenheit is equivalent to {kelvin:.2f} kelvin")