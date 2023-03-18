def kt_kituthuong(st):
    for i in st:
        if (i.islower()):
            return True
    return False
def kt_kituhoa(st):
    for i in st:
        if (i.isupper()):
            return True
    return False
def kt_kituso(st):
    for i in st:
        if (i.isdigit()):
            return True
    return False
def kt_kitudacbiet(st):
    for i in st:
        if (i == '$' or i == '#' or i =='@'):
            return True
    return False
def kt_dodai(st):
    if (6 <= len(st) <= 12):
        return True
    return False

kq = []
matkhau = input("Nhập một chuỗi mật khẩu, cách nhau bởi dấu phẩy: ")
mk = [x for x in matkhau.split(',')]
for i in mk:
    if (kt_kituthuong(i) and kt_kituhoa(i) and kt_kituso(i) and kt_dodai(i) and kt_kitudacbiet(i)):
        kq.append(i)
print(' '.join(kq))