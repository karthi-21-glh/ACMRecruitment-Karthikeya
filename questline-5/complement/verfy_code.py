num=int(input())
if num>127 in num<-128:
    print("Invalid Input")
else:
    if num < 0:
        num = (1 << 8) + num  
    binary_str = ""
    temp = num
    for i in range(8):
        binary_str = str(temp % 2) + binary_str
        temp //= 2
    print(binary_str)
