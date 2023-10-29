"""
Convert Arabic Number to Roman Number.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลขอราบิก เป็นตัวเลขโรมัน
โดยที่ค่าที่รับต้องมีค่ามากกว่า 0 จนถึง 1000

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).
"""

def c_arabic_to_roman(arabic_number):

    if arabic_number < 0 or arabic_number > 1000:
        return "Error!! กรุณาป้อนตัวเลขระหว่าง 1 ถึง 1,000"
    
    if arabic_number == 0:
        return 'Error!! ไม่มีตัวเลข 0 ในระบบตัวเลขโรมัน กรุณาป้อนตัวเลขระหว่าง 1 ถึง 1000'

    roman_numbers = { 
            1000: 'M', 900: 'CM',  500: 'D', 400: 'CD',  100: 'C', 90: 'XC',  
            50: 'L', 40: 'XL', 10: 'X',  9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
        }

    result = ''

    for value, numeral in roman_numbers.items():
        while arabic_number >= value:
            result += numeral
            arabic_number -= value

    return result

try:
    user_input = int(input("ป้อนตัวเลข (1 - 1000): "))
    result = c_arabic_to_roman(user_input)
    print("ตัวเลขโรมัน:", result)
except ValueError:
    print("โปรดป้อนตัวเลขระหว่าง 1 ถึง 1,000")
