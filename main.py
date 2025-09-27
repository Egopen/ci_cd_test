def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Деление на ноль!")
    return a / b


def is_prime_number(n):
    """Проверка числа на простоту"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def calculator():
    print("Простой калькулятор")
    print("Доступные операции: +, -, *, /")

    a = float(input("Введите первое число: "))
    op = input("Введите операцию (+, -, *, /): ")
    b = float(input("Введите второе число: "))

    if op == "+":
        print(f"Результат: {add(a, b)}")
    elif op == "-":
        print(f"Результат: {subtract(a, b)}")
    elif op == "*":
        print(f"Результат: {multiply(a, b)}")
    elif op == "/":
        print(f"Результат: {divide(a, b)}")
    else:
        print("Неизвестная операция!")


if __name__ == "__main__":
    calculator()

    # Проверка числа на простоту
    num = int(input("\nВведите число для проверки на простоту: "))
    if is_prime_number(num):
        print(f"{num} является простым числом.")
    else:
        print(f"{num} не является простым числом.")
