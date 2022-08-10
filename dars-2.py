# LINEAR SEARCH
# Kompyuter fanida chiziqli qidiruv yoki ketma-ket qidiruv ro'yxat ichidagi elementni topish usulidir
# Moslik topilmaguncha yoki butun roʻyxat qidirilmaguncha u roʻyxatning har bir elementini ketma-ket 
# tekshiradi.
# linear algoritm:
# Qiymatlari yoki yozuvlari L 0 .... L n -1 va maqsadli qiymati T bo'lgan n elementdan iborat L ro'yxati
#  berilgan bo'lsa, quyidagi pastki dastur L da maqsadli T indeksini topish uchun chiziqli qidiruvdan 
# foydalanadi .

# i ni 0 ga qo'ying .
# Agar L i = T bo'lsa, qidiruv muvaffaqiyatli yakunlanadi; qaytib i .
# i ni 1 ga oshiring .
# Agar i < n bo'lsa , 2-bosqichga o'ting. Aks holda, qidiruv muvaffaqiyatsiz tugaydi.

# def findNum(N=10):
#     for n in range(1,N):
#         ans = input(f"Siz {n}-o'yladingiz? (y/n)")
#         if ans=='y':
#             print("Yutdim!")
#             return n

# findNum(10)

# BINEAR SEARCH

# Informatika fanida ikkilik qidiruv , shuningdek, yarim intervalli qidiruv , logarifmik qidiruv ,
# yoki ikkilik chop deb nomlanuvchi , tartiblangan massiv ichida maqsadli qiymatning oʻrnini topadigan
#  qidiruv algoritmidir. Ikkilik qidiruv maqsadli qiymatni massivning o'rta elementi bilan
#  taqqoslaydi. Agar ular teng bo'lmasa, nishon yotolmaydigan yarmi yo'q qilinadi va qolgan yarmida
#  qidirish davom etadi, yana o'rta elementni maqsad qiymat bilan taqqoslash uchun olib, maqsad qiymat
#  topilgunga qadar takrorlanadi. Agar qidiruv qolgan yarmi bo'sh bo'lishi bilan tugasa, maqsad massivda emas.

# Oʻrnatish L uchun 0va R uchun n-1.
# Agar L > R, qidiruv muvaffaqiyatsiz tugadi.
# Oʻrnatish m(o'rta elementning pozitsiyasi) ning qavatiga {{L+R}{2}} dan kichik yoki teng eng katta butun son
#  {{L+R}{2}}
# Agar{\displaystyle A_{m}<T}{\displaystyle A_{m}<T}, oʻrnating{\displaystyle L}Luchun{\displaystyle m+1}m+1va
#  2-bosqichga o'ting.
# Agar{\displaystyle A_{m}>T}{\displaystyle A_{m}>T}, oʻrnating{\displaystyle R}Ruchun{\displaystyle m-1}m-1va
#  2-bosqichga o'ting

# def linear_search(list, item):
#     for n in range(len(list)):
#         if list[n]==item:
#             return n
#     return None

# def binary_search(list, item):
#     low = 0
#     high = len(list)-1
#     while low <= high:
#         mid = (low + high)//2
#         guess = list[mid]
#         if guess == item:
#             return mid
#         if guess > item:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return None

# # myList1 = [1,3,4,6,7,8,10,12,23,45,56,78,99]
# # print(linear_search(myList1,11))
# # print(binary_search(myList1,11))

# # myList2 = [18,12,25,1,3,4,10,5,23,4,13,89]
# # myList2.sort()
# # print(linear_search(myList2,13))
# # print(binary_search(myList2,13))

# mevalar = ['olma','anor','olcha','behi','shaftoli','anjir']
# # mevalar.sort()
# print(mevalar)
# print(binary_search(mevalar,'behi'))