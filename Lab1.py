def euclid(a, b):

    if a == 0:
        return b, 0, 1
    nod, x1, y1 = euclid(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    print(f"Текущие значения: a = {a}, b = {b}, nod = {nod}, x = {x}, y = {y}")
    return nod, x, y

def degree_comparison(a, b, m):

    nod, x, y = euclid(a, m)
    print(f"НОД({a}, {m}) = {nod}")

    if b % nod != 0:
        print(f"Уравнение не имеет решений. НОД({a}, {m}) = {nod}, а {b} не делится на {nod},"
              " значит, уравнение не имеет решений в целых числах.")
        return

    x0 = (x * (b // nod)) % (m // nod)
    a //= nod
    b //= nod
    m //= nod
    print(f"Одно из решений: x = {x0} + k * {a} (где k - любое целое число)")

    for k in range(nod):
        total = (x0 + k * (m // nod)) % (m // nod)
        print(f"Решение для k = {k}: x = {total}")

if __name__ == "__main__":
    a = int(input("Введите  a: "))
    b = int(input("Введите  b: "))
    m = int(input("Введите  m: "))
    degree_comparison(a, b, m)
