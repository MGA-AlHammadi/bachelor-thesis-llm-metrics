def process_numbers(numbers):
    total = 0
    try:
        for n in numbers:
            if n % 2 == 0:
                total += n
            else:
                total -= n
        return total
    except TypeError:
        return None

def factorial(n):
    if n < 0:
        raise ValueError("Negative Zahl nicht erlaubt")
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

def find_max(numbers):
    if not numbers:
        return None
    max_value = numbers[0]
    for n in numbers[1:]:
        if n > max_value:
            max_value = n
    return max_value
