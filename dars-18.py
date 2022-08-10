# GREEDY ALGORITHMS

# • Ba'zi muammolar hech qanday algoritmga tushmaydi
# • Shunday holatda bizga ochko'z algoritmlar yordam beradi
# • Ochko'z algoritmlar har qadamda eng optimal yechimni tanlash
# • Har doim ham to'g'ri yechimni bermaydi

# GREEDY ALGORITHMS
# • Quyidagi muammoni ko'ramiz:
# • Bizda sinfxona va quyidagi darslar jadvali bor:
# • Matematika: 9:00-10:00 
# • Fizika: 9:30-10:30 
# • Adabiyot: 10:00-11:00 
# • Informatika: 10:30-11:30
# • Tarix: 11:00-12:00 
# • Berilgan sinfda o'tish mumkin bo'lgan darslar ro'yxatini tuzing 
# • Yechim:
# 1. Eng erta tugaydigan darsni tanlaymiz va ro'yxatga qo'shamiz 
# 2. Ro'yxat oxiridagi darsdan keyin boshlanadigan eng erta darsni tanlaymiz va
# ro'yxatga qo'shamiz. 
# 3. Jadvaldagi darslar tugaguncha 2-qadamni takrorlayveramiz

# • Ochko'z algoritmlar har doim ham eng to'g'ri yechimni bermayd
# • Lekin amalga oshirish (dasturlash) oson
# • Agar to'g'ri yechimni topish juda ko'p vaqt (resurs) talab qilsa
# qoniqarli yechimni topish uchun Greedy Algortimlarni tanlang

# THE SET-COVERING PROBLEM
# • Tasavvur qiling, siz yangi uyali aloqa kompaniyasi uchun shahar
# bo'ylab antenalar o'rnatib chiqishingiz kerak 
# • Sizga antenna o'rnatish uchun 4 ta binoga ruhsat tegdi 
# • Har bir binoga qo'yilgan antenna faqatgina sanoqli hududlarni qamrab oladi 
# • Muammo barcha hududlarni qamraydigan eng kam antennalar ' (binonlarni) toping

# Yechim: 
# 1. Binolarning mavjud kombinasiyalarini quramiz 
# • n ta bino uchun 2n kombinasiya mavjud
# 2. Kombinasiyalar orasidan barcha hudularni qamrab oladiganlarnini topamiz 
# 3. Ularning orasidan eng kam bino bor to'plamni tanlaymiz

