st = input("Nhập đầu vào: ")
#Đưa về một list ứng với các phần tử là các từ
lis = [x for x in st.split()]
#list dem dùng để đếm số từ lặp lại
dem = [1 for x in st.split()]
#Dùng để sắp xếp lis theo bảng chữ cái
lis.sort()
for i in range(len(lis) - 1, 0, -1):
    if (lis[i-1] == lis[i]):
        dem[i-1] += dem[i]
        dem[i] = 0
for i in range(len(lis)):
    if (dem[i] != 0):
        print("{}: {}".format(lis[i],dem[i]))

