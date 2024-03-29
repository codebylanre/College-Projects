
"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      169076507
Email:   olag6507@mylaurier.ca
__updated__ = "2023-06-12"
-------------------------------------------------------
"""

# FOUNDATION CALCULATION
found_length = float(input("Enter foundation length: "))
found_width = float(input("Enter foundation width: "))
found_height = float(input("Enter foundation height: "))
cost_of_conc = float(input("Enter cost of concrete: "))
conc_needed = found_length * found_width * found_height

# WALL CALCULATIONS
wall_height = float(input("Enter Wall height: "))
cost_of_bricks = float(input("Enter cost of bricks: "))
bricks_needed = ((wall_height * found_width) +
                 (wall_height * found_length)) * 2

# PRICES
cost_bricks = bricks_needed * cost_of_bricks
cost_conc = conc_needed * cost_of_conc
total_cost = cost_conc + cost_bricks

"""
print(f"Concrete needed for foundation: {conc_needed:,.2f} m³")
print(f"Cost of concrete:               ${cost_conc:,.2f}")
print(f"Bricks needed for walls:        {bricks_needed:,.2f} m²")
print(f"Cost of bricks:                 ${cost_bricks:,.2f}")
print(f"Total cost:                     ${total_cost:,.2f}")
"""


print(F"""
Concrete needed for foundation: {conc_needed:,.2f} m³
Cost of concrete:               ${cost_conc:,.2f}
Bricks needed for walls:        {bricks_needed:,.2f} m²
Cost of bricks:                 ${cost_bricks:,.2f}
Total cost:                     ${total_cost:,.2f}
""")
