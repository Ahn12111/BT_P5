import math

def xuly(lis, vitri):
    for cachthuc, sobuoc in lis:
        if (cachthuc == "UP"):
            vitri[1] += float(sobuoc)
        if (cachthuc == "DOWN"):
            vitri[1] -= float(sobuoc)
        if (cachthuc == "RIGHT"):
            vitri[0] += float(sobuoc)
        if (cachthuc == "LEFT"):
            vitri[0] -= float(sobuoc)
    return round(math.sqrt(vitri[0]**2 + vitri[1]**2))
    
lis = []
vitri = [0,0]
print("Nhap cac buoc di chuyen: ")
while True:
    st = input()
    if st:
        lis.append(list(st.split()))
    else:
        break
print("Khoang cach so voi vi tri ban dau la: ", xuly(lis, vitri))