"""
3.เขียนโปรแกรมหาจำนวนเลข 0 ที่อยู่ติดกันหลังสุดของค่า factorial ด้วย Python 

*** โดยห้ามใช้ math.factorial เช่น 7! = 5040 มีเลข 0 ต่อท้าย 1 ตัว, 10! = 3628800 มีเลข 0 ต่อท้าย 2 ตัว
"""

def find_trailing_zeros(n):
    count = 0
    while n % 10 == 0:
        count += 1
        n //= 10
    return count

def factorial_with_zeros(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

try:
    number = int(input("ป้อนค่า factorial เป็นจำนวนเต็มบวกเท่านั้น : "))
    if number < 0:
        print("Error!! ป้อนตัวเลขเป็นจำนวนติดลบ (-)")
    else:
        fact_result = factorial_with_zeros(number)
        zeros_count = find_trailing_zeros(fact_result)

        print(f"{number}! = {fact_result} มีจำนวนเลข 0 ต่อท้าย {zeros_count} ตัว")
except ValueError:
    print("Error!! ไม่ได้ป้อนจำนวนตัวเลขเข้ามา")