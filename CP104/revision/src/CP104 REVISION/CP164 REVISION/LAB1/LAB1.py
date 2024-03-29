def near_and_far(a, b, c):
    if abs(b - c) <= 1:
        if abs(a - c) <= 1:
            if abs(b - a) <= 1:
                return True
            
    return False

# print(near_and_far(1, 1, 2))


def sum_without_twenties(a, b, c):
    if a in range(20, 30):
        a = 0
    if b in range(20, 30):
        b = 0
    if c in range(20,  30):
        c = 0

    return a + b + c

# print(sum_without_twenties(10, 24, 40))


def sumDigits(n):
    count = 0
    while n != 0:
        count += n%10
        n //= 10
    
    return count

# print(sumDigits(123))

def get_substring_positions(a, b):
    


def filter_words(filename, unwanted_words):
    return
    
