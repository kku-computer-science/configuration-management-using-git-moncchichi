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