"""Simple calculator used to demonstrate Continuous Integration with GitHub Actions."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def heat_index_category(temp_c):
    """Classify a temperature (deg C) using the IMD plains heatwave thresholds."""
    if temp_c >= 47:
        return "Severe heatwave"
    if temp_c >= 45:
        return "Heatwave"
    if temp_c >= 40:
        return "Hot"
    return "Normal"


if __name__ == "__main__":
    print("2 + 3 =", add(2, 3))
    print("10 / 4 =", divide(10, 4))
    print("46 C is", heat_index_category(46))
