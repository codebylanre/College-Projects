from t01_functions import closest_number

CASES = (
    ([], 5),
    ([99], 23),
    ([1, 2, 3], 7),
    ([-5, 15, 0, 9], 12)
)

for case in CASES:
    print(f'closest_number({case}) → {closest_number(case[0],case[1])}')
    print()


print("MY test")
values = [5, 12, 8, 20, 3]
target = 10


cn = closest_number(values, target)
print(cn) 
