from t03_functions import alternate_case

CASES = ('', 'ABC', 'abc', '123', 'This is the 3rd sentence.')

for case in CASES:
    print(f'alternate_case("{case}") → {alternate_case(case)}')
    print()

print("my test")
string = "Abdulbasit is an immaculate programmer"
alternating = alternate_case(string)
print(alternating)