def calculator():
    print("Калькулятор v1.0")
    
    # Сложение двух чисел
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    
    result = a + b
    print(f"Результат сложения: {result}")
    return result

def main():
    calculator()

if __name__ == "__main__":
    main()