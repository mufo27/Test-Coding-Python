"""
2.เขียนโปรแกรมหา index ของตัวเลขที่มีค่ามากที่สุดใน Array ด้วยภาษา python เช่น [1,2,1,3,5,6,4] ลำดับที่มีค่ามากที่สุด คือ index = 5 

*** โดยไม่ให้ใช้ฟังก์ชั่นที่มีอยู่แล้ว ให้ใช้แค่ลูปกับการเช็คเงื่อนไข
"""


def find_max_index(arr):
    max_value = arr[0]
    max_index = 0

    for i in range(1, len(arr)):
        if arr[i] > max_value:
            max_value = arr[i]
            max_index = i

    return max_index

try:
    user_input = input("ป้อนค่าอาร์เรย์ โดยใช้เครื่องหมายจุลภายใน (,) เช่น 1,2,3,4 : ")
    user_array = [int(x) for x in user_input.split(",")]
    result = find_max_index(user_array)
    print("ลำดับที่มีค่ามากที่สุด คือ index :", result)
except ValueError:
    print("Error!! โปรดป้อนอาร์เรย์ที่ถูกต้อง")
