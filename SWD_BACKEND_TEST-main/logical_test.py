"""
Convert Number to Thai Text.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลข เป็นตัวหนังสือภาษาไทย
โดยที่ค่าที่รับต้องมีค่ามากกว่าหรือเท่ากับ 0 และน้อยกว่า 10 ล้าน

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""

thai_numbers = ("ศูนย์", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า")
thai_units = ("", "สิบ", "ร้อย", "พัน", "หมื่น", "แสน", "ล้าน")

def unit_process(val):
    
    length = len(val) > 1
    result = ''

    for index, cur_val in enumerate(map(int, val)):
        if cur_val:
            if index:
                result = thai_units[index] + result

            if length and cur_val == 1 and index == 0:
                result += 'เอ็ด'
            elif index == 1 and cur_val == 2:
                result = 'ยี่' + result
            elif index != 1 or cur_val != 1:
                result = thai_numbers[cur_val] + result

    return result

def c_number_to_thai_txt(number):

    if number < 0 or number > 10000000:
        return "Error!! กรุณาป้อนตัวเลขระหว่าง 0 ถึง 10,000,000"

    if number == 0:
        return thai_numbers[0]
    
    s_number = str(number)[::-1]
    n_list = [s_number[i:i + 6].rstrip("0") for i in range(0, len(s_number), 6)]
    result = unit_process(n_list.pop(0))

    for i in n_list:
        result = unit_process(i) + 'ล้าน' + result

    return result

try:
    user_input = int(input("ป้อนตัวเลข (0 - 10,000,000) : "))
    result = c_number_to_thai_txt(user_input)
    print("คำอ่านภาษาไทย : ", result)
except ValueError:
    print("โปรดป้อนตัวเลขระหว่าง 0 ถึง 10,000,000")
