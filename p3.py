# 3. นับจํานวนสระในสตริงที่กําหนดให้โดยใช้ `for loop` [เฉลย](https://cdn.discordapp.com/attachments/581018943041306641/1088990752299827200/image.png)
    
#     กำหนดให้  
    
#     - ตัวแปร `string` = "Hello, World!”
#     - ตัวแปรสระหรือ `vowels` = "aeiouAEIOU”
#     - ลองใช้ if `char` in `vowels` เพื่อเป็นตรวจสอบว่า `char` นั้นๆมีอยู่ใน `vowels` มั้ย
#     - ผลลัพธ์ที่คาดหวัง : จำนวนสระคือ: 3

string = "fruits"
vowels = "aeiouAEIOU"
count = 0
for char in string:
    if char in vowels:
        count += 1 
# f"{}" "{}".format()
print("จำนวนสระคือ {}".format(count))