# 2. print คํานวณผลรวมของตัวเลขทั้งหมดตั้งแต่ 1 ถึง 100 โดยใช้ `for loop` [เฉลย](https://cdn.discordapp.com/attachments/581018943041306641/1088990321477685338/image.png)
    
#     กำหนดให้
    
#     - สร้าวตัวแปล total ขึ้นมา แล้วบวกตัวมันเอง total = total + total
#     - ผลลัพธ์ที่คาดหวัง : 5050
total = 0
for i in range(1,101):
    total += i
    
print(total)