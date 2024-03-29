"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      169076507
Email:   olag6507@mylaurier.ca
__updated__ = "2023-06-23"
-------------------------------------------------------
"""

from functions import pollution_category

air_quality_index = int(input("Enter AQI: "))

pollution = pollution_category(air_quality_index)

print(f"pollution_category ({air_quality_index}) = {pollution}")
