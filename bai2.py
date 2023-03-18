#hoán đổi hai phần tử trong list, hai vị trí hoán đổi là j và k
def hoandoi(lis, j, k):
    tam = lis[j]
    lis[j] = lis[k]
    lis[k] = tam
def xuly(lis):
    for i in range(3):
        for j in range(len(lis)):
            for k in range(j, len(lis)):
                #nếu phần tử tại ví trí (j,i) > phần tử tại vị trí (k,i) thì hoán đổi cho nhau
                if ((lis[j][i] > lis[k][i]) and (kt[j] == kt[k] == 1)):
                    hoandoi(lis, j, k)
        for j in range(len(kt)):
            kt[j] = 0
        #Dòng này mục đích để kiểm tra nếu tên của hai vị trí này bằng nhau thì kt tại hai vị trí này gán bằng 1 để so sánh phần tiếp theo.
        for j in range(len(lis) - 1):
            if (lis[j][i] == lis[j+1][i]):
                kt[j] = kt[j+1] = 1

lis =[]
#kt là một list dùng để kiểm tra xem các phần tử trùng nhau
kt = []
print("Nhap dau vao: ")
while True:
    st = input()
    if st:
        lis.append(tuple(st.split(',')))
        kt.append(1)
    else: break
xuly(lis)
print(lis)