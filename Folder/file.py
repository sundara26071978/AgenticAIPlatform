def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def divide(a: int, b: int) -> float:
    """Divide two numbers, raising an error if division by zero is attempted."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
