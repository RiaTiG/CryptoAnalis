def task(p):
    """Находит и выводит квадратичные вычеты/невычеты с пояснениями"""
    if p <= 2 or not all(p % i != 0 for i in range(2, int(p**0.5)+1)):
        print(f"Ошибка: {p} не является простым числом > 2")
        return None, None
    
    print(f"Анализ квадратичных вычетов для простого модуля p = {p}\n")
    exponent = (p-1) // 2
    residues = set()
    non_residues = set()
    print(f"1. Вычисляем показатель (p-1)/2 = ({p}-1)/2 = {exponent}\n")
    
    print(f"2. Проверяем числа от 1 до {p-1}:\n")
    for a in range(1, p):
        calculation = f"{a}^{exponent} mod {p}"
        power = a ** exponent
        mod_result = power % p
        result_type = "вычет" if mod_result == 1 else "невычет"
        
        print(f" {calculation:10} = {str(power):>5} mod {p} = {mod_result:2} {result_type}")
        if mod_result == 1:
            residues.add(a)
        else:
            non_residues.add(a)
    
    print(f"\n3. Результаты:")
    print(f"   Квадратичные вычеты: {residues}")
    print(f"   Квадратичные невычеты: {non_residues}")
    return residues, non_residues

if __name__ == "__main__":
    a = int(input("Введите  a: "))
    task(a)
