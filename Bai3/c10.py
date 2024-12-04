import math
def Tinh(R):
    if R <= 0:
        print ("Ban kinh khong hop le! Ban kính khởng phai la mot so duong.")
        return
    chu_vi = 2 * math.pi * R
    dien_tich = math.pi * R ** 2
    print (f"Chu vi cua hinh tron voi ban kinh {R} la: {chu_vi:.2f}")
    print ("Dien tich cua hinh tron voi ban kinh {R} la: {dien_tich:.2f}")
try:
    R = float(input("Nhap ban kinh cua hinh tron: ") )
    Tinh (R)
except ValueError:
    print ("Gia tri ban kinh khong hop le! Vui long nhap mot so.")
