def xuly(n):
    i = 0
    while (i < n):
        j = i
        i += 1
        if j % 7 == 0:
            #yield là hàm trả về tạm thời, rồi vẫn tiếp tục chạy
            yield j

n = int(input("Nhập n: "))
print("Cac só chia het cho 7: ")
for i in xuly(n):
    print(i)
