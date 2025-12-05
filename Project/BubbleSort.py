# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

#1 รับ Input เป็น interger
user_input = input("กรุณากรอกจำนวนเต็มคั่นด้วยช่องว่าง: ")
arr = [int(x) for x in user_input.split()]
