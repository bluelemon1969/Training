test = [1,2,3,4,5,6]

test2 = [7,8,9,10]

test += test2
length = len(test)

yahoo = "鎌倉幕府"

strsum = 0
intsum = 0

#print(length)

yahoo

for cnt in test:
    print(cnt)
    if cnt == 2 & test[cnt-1] == 2 :
        print("2だよ")
    elif cnt == 5:
        print("5だよ")
    else:
        print(test[cnt-1])

    intsum += test[cnt-1]
    strsum = sum(test)
    print ("intsumは：" , intsum)
    print ("strsumは：" , strsum)

for cnt2 in range(length):
    print(test[cnt2])
