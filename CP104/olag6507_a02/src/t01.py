"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      169076507
Email:   olag6507@mylaurier.ca
__updated__ = "2023-06-08"
-------------------------------------------------------
"""
# PROGRAM TO CALCULATE ANNUAL TAX PAID BY AN INVESTOR
TAX_RATE = 5.25 / 100

total_dividends = float(input("Enter the projected total dividends: $"))

tax_pay = total_dividends * TAX_RATE


print(f"Total dividends:   ${total_dividends:,.2f}")
print(f"Annual tax:        %{TAX_RATE*100}")
print(f"Tax:               ${tax_pay:,.2f}")


#print(f"Tax:   $ {tax_pay:,.2f}")

#print(f"The tax to be paid on ${total_dividends:,.2f} is $ {tax_pay:,.2f}")


#print(f"Your tax is ${tax_pay:,.2f}")


"""
print("\nProjected Tax Report")
print("-----------------------------")
print(f"Total dividends:   ${total_dividends:,.2f}")
print(f"Annual tax:        %{TAX_RATE*100}")
print("-----------------------------")
print(f"Tax:               ${tax_pay:,.2f}")
"""
