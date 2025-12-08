# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

#1 รับ Input 
#ค่าที่ 1 input สำหรับ sort (Integer)
user_input = input("กรุณากรอกจำนวนเต็มคั่นด้วยช่องว่าง: ")
arr = [int(x) for x in user_input.split()]
#ค่าที่ 2 ตัวเลือก algorithm
print("เลือกอัลกอริทึมที่จะใช้แทนด้วยเลข 1 คือ Quick Sort และ 2 คือ Bubble Sort")
choice = input("กรุณาเลือกอัลกอริทึม (1 หรือ 2): ")

#Quick Sort Algorithm
def quick_sort(array):
    # ถ้า array มี 0 ตัว หรือ 1 ตัว = ไม่ต้องเรียงแล้วส่งกลับเลย
    if len(array) <= 1:
        return array

    # เลือก pivot = ค่าตรงกลางของ array
    pivot = array[len(array) // 2]

    # สร้าง list 3 กอง
    # left  = ค่าที่น้อยกว่า pivot
    # middle = ค่าที่เท่ากับ pivot เผื่อมีค่าซ้ำ
    # right = ค่าที่มากกว่า pivot
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]

    # เรียงซ้ำเฉพาะ left และ right แล้วต่อผลลัพธ์เข้าด้วยกัน
    return quick_sort(left) + middle + quick_sort(right)

# เลือก algorithm
if choice == "1":
    print("You choose Quick Sort")
    result = quick_sort(arr)
    print("Result:", result)

elif choice == "2":
    print("You choose Bubble Sort")
    #เติม about Bubble Sort

else:
    print("You can choose only 1 or 2")
