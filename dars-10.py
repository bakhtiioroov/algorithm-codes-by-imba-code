# Kompyuter fanida divide and conquer - algoritm dizayn paradigmasi . divide-and-conquer algoritmi muammoni
# rekursiv ravishda bir xil yoki o'zaro bog'liq turdagi ikki yoki undan ortiq kichik muammolarga ajratadi,
# toki ular to'g'ridan-to'g'ri hal qilish uchun etarlicha sodda bo'ladi. Keyin kichik muammolarning echimlari
# birlashtirilib, asl muammoga yechim topiladi.

# “divide-and-conquer” texnikasi ko‘plab muammolarni hal qilish uchun samarali algoritmlarning asosini tashkil
# etadi, masalan, saralash (masalan, tezkor saralash , birlashtirish sort ), katta sonlarni ko‘paytirish 
# (masalan, Karatsuba algoritmi ), eng yaqin nuqtalar juftligini topish , sintaktik tahlil 
# ( masalan, yuqoridan pastga tahlil qiluvchilar ) va diskret Furye konvertatsiyasini hisoblash ( FFT ).

# Muammoni bir xil muammoning kichikroq misollari bo'lgan bir nechta kichik muammolarga ajrating.
# 
#  Kichik muammolarni rekursiv yechish orqali yengib chiqing. Agar ular etarlicha kichik bo'lsa,
#  kichik muammolarni asosiy holatlar sifatida hal qiling.

#  Kichik muammolarning yechimlarini asl muammoning yechimiga birlashtiring.

# def gcd(a,b):
#     if a==0:
#         return b
#     if a>b:
#         a,b=b,a    
#     return gcd(b-a,a)

# if __name__ == '__main__':
#     print(gcd(168,64))