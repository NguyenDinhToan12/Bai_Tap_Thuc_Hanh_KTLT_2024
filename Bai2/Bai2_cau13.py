import math
a = float(input("Nhap he so a: "))
b = float(input("Nhap he so b: "))
c = float(input("Nhap he so c: "))
delta = b**2 - 4*a*c
if a == 0:
    if b ==0:
       if c ==0:
           print ("phuong trinh co vo so nghiem.")
       else:
           print ("phuong trinh vo nghiem.")
    else:
        x = -с / b
        print (f"phuong trinh co mot nghiem: x = {x}")
else:
    if delta < 0:
       print("phuong trinh vo nghiem.")
    elif delta == 0:
        x = -b / (2*a)
        print (f"phuong trinh co nghiem kep: x = {x}")
    else:
        x1 = (-b + math.sprt (detal)) / (2*a)
        x2 = (-b - math.sprt (detal)) / (2*a)
        print (f"phuong trinh co hai nghiem phan biet: x1 = {1}, x2 = {2}")
