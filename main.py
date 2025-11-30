def calculator():
    print("Калькулятор v2.0")
    
    # Умножение двух чисел
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    
    result = a * b
    print(f"Результат умножения: {result}")
    return result

def additional_function():
    print("Дополнительная функция в ветке 2")

def main():
    calculator()
    additional_function()

if __name__ == "__main__":
    main()