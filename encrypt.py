from pickle import TRUE
import sys

# 儲存input
method = sys.argv[2] 
input = sys.argv[4]
key = sys.argv[6]
ciphertext = ''

if(method == "caesar"):
    key = int(key)
    key = key % 26
    for i in range(len(input)):
        asc = ord(input[i]) + key
        if asc < 97:
            asc += 26
        elif asc > 122:
            asc -= 26
        asc -= 32

        char = chr(asc)
        ciphertext += char
   
elif(method == "playfair"):
    
    # 建立 Key Matrix
    matrix =''
    for i in range(0,26):
        matrix += chr(97 + i)
    matrix = matrix.replace('j', '')
    for i in range(len(key)):
        matrix = matrix.replace(key[i], '')
    matrix = key + matrix

    index = 0
    while TRUE:

        if(index >= len(input)):
            break

        # 前面字母位置
        for i in range(0,25):
            if(input[index] == matrix[i]):
                pos1 = i
                break
        if(index == len(input) -1 or input[index] == input[index + 1]):
            for i in range(0, 25):
                if('x' == matrix[i]):
                    pos2 = i
                    index += 1
                    break
        else:      
            for i in range(0,25):
                if(input[index + 1] == matrix[i]):
                    pos2 = i
                    index += 2
                    break

        # 同row
        if(int(pos1 / 5) == int(pos2 / 5)):
            # print("row")
            if(pos1 % 5 == 4):
                pos1 -= 4
            else:
                pos1 += 1

            if(pos2 % 5 == 4):
                pos2 -= 4
            else:
                pos2 += 1
        
        # 同column
        elif(int(pos1 % 5) == int(pos2 % 5)):
            # print("col")
            if(pos1 >= 20):
                pos1 -= 20
            else:
                pos1 += 5

            if(pos2 >= 20):
                pos2 -= 20
            else:
                pos2 += 5
        else:
            temp = pos1
            pos1 = pos1 + (pos2 % 5 - pos1 % 5)
            pos2 = pos2 + (temp % 5 - pos2 % 5)

        ciphertext += matrix[pos1]
        ciphertext += matrix[pos2]

    ciphertext = ciphertext.upper()
                       
elif(method == "vernam"):

    # key 長度不足時補上
    if len(key) < len(input):
        key = key + input
        key = key[:len(input)]

    for i in range(len(input)):

        inasc = ord(input[i]) -97
        keyasc = ord(key[i]) - 97
        inbin = ''
        keybin = ''
        # input, key 轉換成 binary
        for j in range(0,5):
            if inasc % 2 == 0:
                inbin = '0' + inbin
            else:
                inbin = '1' + inbin
            inasc = int(inasc/2)

            if keyasc % 2 == 0:
                keybin = '0' + keybin
            else:
                keybin = '1' + keybin
            keyasc = int(keyasc/2)

        outputbin=''
        outputasc = 0
        for j in range(0,5):
            if inbin[j] != keybin[j]:
                outputasc += pow(2,4-j)
        ciphertext += chr(outputasc + 65)

elif(method == "railfence"):


    key = int(key)

    for i in range(key):

        delta = 0
        index = i
        ciphertext += input[index]

        while TRUE:
            
            delta = 2 * (key - i - 1) 
            # print(index,delta)
            if index + delta >= len(input):
                break
            else:
                if delta != 0:
                    index += delta
                    #print(index, input[index])
                    ciphertext += input[index]

            delta = 2 * i
            # print(delta)
            if index + delta >= len(input):
                break
            else:
                if delta != 0:
                    index += delta
                    #print(index, input[index])
                    ciphertext +=input[index]

    ciphertext = ciphertext.upper()

elif(method == "row"):

    # for迴圈次數
    if len(input) % len(key) == 0:
        iteration = int(len(input) / len(key))
    else:
        iteration = int(len(input) / len(key)) + 1

    for i in range(1,len(key) + 1):
            for j in range(len(key)):
                if(int(key[j]) == i): #先找到要append哪行
                    for k in range(iteration):
                        if(int(key[j]) == i):
                            if k * len(key) + j >= len(input):
                                break
                            ciphertext += input[k * len(key) + j]
        

    ciphertext = ciphertext.upper()

print(ciphertext)



        
   


       

