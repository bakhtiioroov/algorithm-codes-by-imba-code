# Stack - bu ko'pchilik dasturlash tillarida keng qo'llaniladigan mavhum ma'lumotlar turi (ADT).
# U stek deb ataladi, chunki u o'zini haqiqiy dunyo stekiga o'xshatadi, masalan - kartalar 
# to'plami yoki plastinkalar to'plami va boshqalar

# Bu xususiyat uni LIFO ma'lumotlar tuzilishiga aylantiradi. LIFO so'zining qisqartmasi
# "Oxirgi kelgan birinchi" degan ma'noni anglatadi. Bu erda oxirgi joylashtirilgan
# (qo'shilgan yoki qo'shilgan) element birinchi bo'lib ochiladi. Stek terminologiyasida kiritish
# operatsiyasi PUSH operatsiyasi, olib tashlash esa POP operatsiyasi deb ataladi.

# Stek Massiv, Struktura, Pointer va Bog'langan ro'yxat yordamida amalga oshirilishi mumkin.
# Stack qat'iy o'lchamli bo'lishi mumkin yoki dinamik o'lchamni o'zgartirish hissi bo'lishi
# mumkin. Bu erda biz stekni massivlar yordamida amalga oshirmoqchimiz, bu esa uni qattiq
# o'lchamdagi stekni amalga oshirishga imkon beradi

# Yangi ma'lumotlar elementini stekga joylashtirish jarayoni Push Operation deb nomlanadi. Surish
#  jarayoni bir qator bosqichlarni o'z ichiga oladi -

# 1-qadam - to'plam to'lganligini tekshiradi.

# 2-qadam - Agar stek to'lgan bo'lsa, xato va chiqishni keltirib chiqaradi.

# 3-qadam - Agar stek to'liq bo'lmasa, yuqoridan keyingi bo'sh joygacha ko'tariladi.

# 4-qadam - Ma'lumotlar elementini stek joylashgan joyiga qo'shadi, bu erda tepa ko'rsatilgan.

# 5-qadam - Muvaffaqiyatni qaytaradi.

# The Stack ustida amallar
# • Push - element qo'shish 
# • Pop - element sug'urib olish 
# • isEmpty – to'plam bo'sh ekanligini tekshirish 
# • isFull – to'plam to'la ekanligini tekshirish 
# • Peek – eng yuqoridagi element qiymatini ko'rish

# class Stack:
#     """Stack obyekti"""
#     def __init__(self):
#         self.stack = []
    
#     def isEmpty(self):
#         """Bo'sh ekanligini tekshirish"""
#         return len(self.stack)==0
    
#     def push(self,data):
#         """Element qo'shish"""
#         self.stack.append(data)
#         return True
    
#     def pop(self):
#         """Element sug'urib olish"""
#         if self.isEmpty():
#             return "Stack is empty"
#         else:
#             return self.stack.pop()
    
#     def peek(self):
#         """Eng ustki elementni ko'rish"""
#         if self.isEmpty():
#             return "Stack is empty"
#         else:
#             return self.stack[-1]

# if __name__=='__main__':
#     stack = Stack()
#     stack.push(5)
#     stack.push(6)
#     stack.push(7)
#     print("Top element: ", stack.peek())
#     print(stack.pop())
#     print(stack.pop())
#     print(stack.pop())
#     print(stack.pop())

