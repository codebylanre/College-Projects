from t02_functions import prime_stats

CASES = (
    ([4, 9, 19, 237, 105, 20, 2, 67, 77, 125, 389, 45, 680, 38]),
    ([87, 34, 76, 59, 22, 93, 47, 12, 85, 67]),
    [45, 71, 23, 98, 56, 14, 89, 32, 61, 27]
)

for case in CASES:
    print(f'prime_stats({case}) → {prime_stats(case)}')
    print()


print("my test")
numbers = [2,3,4,5,6,7]
primes, count, maximum, minimum, average = prime_stats(numbers)
