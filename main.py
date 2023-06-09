
    

    
# 4. print เลขคู่ทั้งหมดระหว่าง 1 ถึง 20 โดยใช้ `for loop` [เฉลย](https://cdn.discordapp.com/attachments/581018943041306641/1088991981457379328/image.png)
#     - ผลลัพธ์ที่คาดหวัง : 2\n6\n8\n10\n12\n14\n16\n18\n20
#     - \n คือ newline หรือบรรทัดใหม่
    
# 5. ค้นหาจํานวนที่มากที่สุดในรายการที่กําหนดโดยใช้ `for loop` [เฉลย](https://cdn.discordapp.com/attachments/581018943041306641/1088992541342449705/image.png)
    
#     กำหนดให้
    
#     - numbers = [10, 5, 20, 3, 15]
#     - สร้างตัวแปรสักตัวเข้ามาเก็บสมาชิกใน `numbers` สักตัวนึงก่อน
#     - ผลลัพธ์ที่คาดหวัง : จํานวนที่มากที่สุด: 20
# 6. สร้างเกมเดาอย่างง่ายที่ผู้ใช้ต้องเดาตัวเลขสุ่มระหว่าง 1 ถึง 10 โดยใช้ while loop [เฉลย](https://cdn.discordapp.com/attachments/581018943041306641/1088995461123285013/image.png)
    
#     กำหนดให้
    
#     - import random เป็นตัวแปรสุ่มตัวเลข
#     - number = random.randint(1, 10) คือการสุ่มตัวเลขตั้ง 1 - 10
#     - guess = int(input("Guess the number between 1 and 10: "))
#     - ผลลัพธ์ที่คาดหวัง : ถ้าผู้ใช้ตอบถูกจะขึ้น Congratulations, you guessed the number! ถ้าผู้ใช้ตอบผิดจะมีบอกใบ้ให้ถ้าน้อยไปจะบอก Too low! ถ้ามากไปจะบอก  Too high!
    
# 7. ออกแบบโปรแกรมคำนวณเกรด โดยรับข้อมูลจากผู้ใช้งานเข้ามา หรือ input โดยมีเงื่อนไขดังนี้โดยใช้ while loop [เฉลย](https://cdn.discordapp.com/attachments/581018943041306641/1088995925315309629/image.png)
#     - ถ้าคะแนนมากกว่าหรือเท่ากับ 80 และ ไม่เกิน 100 แสดงผล `Grade A`
#     - ถ้าคะแนนมากกว่าหรือเท่ากับ 75 และ ไม่เกิน 79 แสดงผล `Grade B+`
#     - ถ้าคะแนนมากกว่าหรือเท่ากับ 70 และ ไม่เกิน 74 แสดงผล `Grade B`
#     - ถ้าคะแนนมากกว่าหรือเท่ากับ 65 และ ไม่เกิน 69 แสดงผล `Grade C+`
#     - ถ้าคะแนนมากกว่าหรือเท่ากับ 60 และ ไม่เกิน 64 แสดงผล `Grade C`
#     - ถ้าคะแนนมากกว่าหรือเท่ากับ 55 และ ไม่เกิน 59 แสดงผล `Grade D+`
#     - ถ้าคะแนนมากกว่าหรือเท่ากับ 50 และ ไม่เกิน 54 แสดงผล `Grade D`
#     - ถ้าน้อยกว่า 50 แสดงผล `Grade F`
#     - คำนวณเกรดไปเรื่อยๆจนกว่าผู้ใช้จะกรอกเลข 0 ถึงจะหยุดการทำงาน
#     - ผลลัพธ์ที่คาดหวัง : กรอก 49 แสดงผลเกรด `Grade F` และ ถ้าผู้ใช้กรอก 0 โปรแกรมจะหยุดทำงาน
    
# 8. ออกแบบโปรแกรมคำนวณค่าดัชนีมวลกาย BMI (Body Mass Index) โดยรับข้อมูลจากผู้ใช้งานสองค่าคือ น้ำหนัก และ ส่วนสูง [เฉลย](https://cdn.discordapp.com/attachments/581018943041306641/1088998216009273475/image.png)
#     - โดยใช้สูตร `น้ำหนัก / (ส่วนสูง ยกกำลัง 2)`
#     - ค่าที่ได้น้อยกว่า 18.5 ให้แสดงข้อความว่า “คุณผอมเกินไป”
#     - ค่าที่ได้อยู่ระหว่าง 18.5-24.9 ให้แสดงข้อความว่า “คุณอยู่เกณฑ์เหมาะสม นํ้าหนักตัวปกติ”
#     - ค่าที่ได้อยู่ระหว่าง 25-29.9 ให้แสดงข้อความว่า “คุณนํ้าหนักเกิน แต่ยังไม่เรียกว่าอ้วน”
#     - ค่าที่ได้อยู่ระหว่าง 30-39.9 ให้แสดงข้อความว่า “คุณอ้วนแล้ว !”
#     - ค่าที่ได้มากกว่าหรือเท่ากับ 40 ให้แสดงข้อความว่า “คุณอ้วนเกินไป อันตรายมาก !!!”
#     - หากแสดงผลลัพธ์หลังคำนวณแล้วให้ถามผู้ใช้งานว่า ต้องการคำนวณต่อหรือไม่ (y/n) ถ้าผู้ใช้ตอบ n จะหยุดการทำงาน
#     - ผลลัพธ์ที่คาดหวัง :  กรุณากรอกน้ำหนักของคุณ (kg): 59
#                                   กรุณากรอกส่วนสูงของคุณ (m): 160
#                                   ค่าดัชนีมวลกายของคุณคือ 0.00
#                                   คุณผอมเกินไป
#                                   ต้องการคำนวณต่อหรือไม่ (y/n): n