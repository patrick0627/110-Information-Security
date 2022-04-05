import sys

# string into list
def string2list(string):
	list1=[]
	list1[:0]=string
	return list1

# first permutation
def firstPermutation(list, input):

    list[0], list[1], list[2], list[3], list[4], list[5], list[6], list[7] \
    = input[57], input[49], input[41], input[33], input[25], input[17], input[9], input[1]

    list[8], list[9], list[10], list[11], list[12], list[13], list[14], list[15] \
    = input[59], input[51], input[43], input[35], input[27], input[19], input[11], input[3]

    list[16], list[17], list[18], list[19], list[20], list[21], list[22], list[23] \
    = input[61], input[53], input[45], input[37], input[29], input[21], input[13], input[5]

    list[24], list[25], list[26], list[27], list[28], list[29], list[30], list[31] \
    = input[63], input[55], input[47], input[39], input[31], input[23], input[15], input[7]

    list[32], list[33], list[34], list[35], list[36], list[37], list[38], list[39] \
    = input[56], input[48], input[40], input[32], input[24], input[16], input[8], input[0]

    list[40], list[41], list[42], list[43], list[44], list[45], list[46], list[47] \
    = input[58], input[50], input[42], input[34], input[26], input[18], input[10], input[2]

    list[48], list[49], list[50], list[51], list[52], list[53], list[54], list[55] \
    = input[60], input[52], input[44], input[36], input[28], input[20], input[12], input[4]

    list[56], list[57], list[58], list[59], list[60], list[61], list[62], list[63] \
    = input[62], input[54], input[46], input[38], input[30], input[22], input[14], input[6]

    return list

def finalPermutation(list, input):
    list[0], list[1], list[2], list[3], list[4], list[5], list[6], list[7]\
    = input[39], input[7], input[47], input[15], input[55], input[23], input[63], input[31]

    list[8], list[9], list[10], list[11], list[12], list[13], list[14], list[15]\
    = input[38], input[6], input[46], input[14], input[54], input[22], input[62], input[30]

    list[16], list[17], list[18], list[19], list[20], list[21], list[22], list[23]\
    = input[37], input[5], input[45], input[13], input[53], input[21], input[61], input[29]

    list[24], list[25], list[26], list[27], list[28], list[29], list[30], list[31]\
    = input[36], input[4], input[44], input[12], input[52], input[20], input[60], input[28]

    list[32], list[33], list[34], list[35], list[36], list[37], list[38], list[39]\
    = input[35], input[3], input[43], input[11], input[51], input[19], input[59], input[27]

    list[40], list[41], list[42], list[43], list[44], list[45], list[46], list[47]\
    = input[34], input[2], input[42], input[10], input[50], input[18], input[58], input[26]

    list[48], list[49], list[50], list[51], list[52], list[53], list[54], list[55]\
    = input[33], input[1], input[41], input[9], input[49], input[17], input[57], input[25]

    list[56], list[57], list[58], list[59], list[60], list[61], list[62], list[63]\
    = input[32], input[0], input[40], input[8], input[48], input[16], input[56], input[24]

    return list 

def PC1(list, input):
    
    list[0], list[1], list[2], list[3], list[4], list[5], list[6], list[7] \
    = input[56], input[48], input[40], input[32], input[24], input[16], input[8], input[0]

    list[8], list[9], list[10], list[11], list[12], list[13], list[14], list[15] \
    = input[57], input[49], input[41], input[33], input[25], input[17], input[9], input[1]

    list[16], list[17], list[18], list[19], list[20], list[21], list[22], list[23] \
    = input[58], input[50], input[42], input[34], input[26], input[18], input[10], input[2]

    list[24], list[25], list[26], list[27], list[28], list[29], list[30], list[31] \
    = input[59], input[51], input[43], input[35], input[62], input[54], input[46], input[38]

    list[32], list[33], list[34], list[35], list[36], list[37], list[38], list[39] \
    = input[30], input[22], input[14], input[6], input[61], input[53], input[45], input[37]
    
    list[40], list[41], list[42], list[43], list[44], list[45], list[46], list[47] \
    = input[29], input[21], input[13], input[5], input[60], input[52], input[44], input[36]

    list[48], list[49], list[50], list[51], list[52], list[53], list[54], list[55] \
    = input[28], input[20], input[12], input[4], input[27], input[19], input[11], input[3]

    return list

def PC2(list, input):
    list[0], list[1], list[2], list[3], list[4], list[5] \
    = input[13], input[16], input[10], input[23], input[0], input[4]

    list[6], list[7], list[8], list[9], list[10], list[11] \
    = input[2], input[27], input[14], input[5], input[20], input[9]

    list[12], list[13], list[14], list[15], list[16], list[17] \
    = input[22], input[18], input[11], input[3], input[25], input[7]

    list[18], list[19], list[20], list[21], list[22], list[23] \
    = input[15], input[6], input[26], input[19], input[12], input[1]

    list[24], list[25], list[26], list[27], list[28], list[29] \
    = input[40], input[51], input[30], input[36], input[46], input[54]

    list[30], list[31], list[32], list[33], list[34], list[35] \
    = input[29], input[39], input[50], input[44], input[32], input[47]

    list[36], list[37], list[38], list[39], list[40], list[41] \
    = input[43], input[48], input[38], input[55], input[33], input[52]

    list[42], list[43], list[44], list[45], list[46], list[47] \
    = input[45], input[41], input[49], input[35], input[28], input[31]

    return list

def Expansion(list, input):

    list[0], list[1], list[2], list[3], list[4], list[5]\
    = input[31], input[0], input[1], input[2], input[3], input[4]

    list[6], list[7], list[8], list[9], list[10], list[11]\
    = input[3], input[4], input[5], input[6], input[7], input[8]

    list[12], list[13], list[14], list[15], list[16], list[17]\
    = input[7], input[8], input[9], input[10], input[11], input[12]

    list[18], list[19], list[20], list[21], list[22], list[23]\
    = input[11], input[12], input[13], input[14], input[15], input[16]

    list[24], list[25], list[26], list[27], list[28], list[29]\
    = input[15], input[16], input[17], input[18], input[19], input[20]

    list[30], list[31], list[32], list[33], list[34], list[35]\
    = input[19], input[20], input[21], input[22], input[23], input[24]

    list[36], list[37], list[38], list[39], list[40], list[41]\
    = input[23], input[24], input[25], input[26], input[27], input[28]

    list[42], list[43], list[44], list[45], list[46], list[47]\
    = input[27], input[28], input[29], input[30], input[31], input[0]

    return list

def XOR(output,expansion, key, round):
    
    for i in range(0, round):
        if(expansion[i] != key[i]):
            output[i] = '1'
        else:
            output[i] = '0'

    return output

def Permutation(list, input):

    list[0], list[1], list[2], list[3], list[4], list[5], list[6], list[7]\
    = input[15], input[6], input[19], input[20], input[28], input[11], input[27], input[16]

    list[8], list[9], list[10], list[11], list[12], list[13], list[14], list[15]\
    = input[0], input[14], input[22], input[25], input[4], input[17], input[30], input[9]

    list[16], list[17], list[18], list[19], list[20], list[21], list[22], list[23]\
    = input[1], input[7], input[23], input[13], input[31], input[26], input[2], input[8]

    list[24], list[25], list[26], list[27], list[28], list[29], list[30], list[31]\
    = input[18], input[12], input[29], input[5], input[21], input[10], input[3], input[24]

    return list

def rotate(list, amount):
    temp =[None] * 28
    for i in range(0,28):
        
        if(i + amount > 27):
            index = i + amount - 28
        else:
            index = i + amount
        temp[i] = list[index]
    return temp

sbox1 = [[14,0,4,15],[4,15,1,12],[13,7,14,8],[1,4,8,2],[2,14,13,4],[15,2,6,9],[11,13,2,1],[8,1,11,7],[3,10,15,5],[10,6,12,11],\
    [6,12,9,3],[12,11,7,14],[5,9,3,10],[9,5,10,0],[0,3,5,6],[7,8,0,13]]

sbox2 = [[15,3,0,13],[1,13,14,8],[8,4,7,10],[14,7,11,1],[6,15,10,3],[11,2,4,15],[3,8,13,4],[4,14,1,2],[9,12,5,11],[7,0,8,6], \
    [2,1,12,7],[13,10,6,12],[12,6,9,0],[0,9,3,5],[5,11,2,14],[10,5,15,9]]

sbox3 = [[10,13,13,1],[0,7,6,10],[9,0,4,13],[14,9,9,0],[6,3,8,6],[3,4,15,9],[15,6,3,8],[5,10,0,7],[1,2,11,4],[13,8,1,15], \
    [12,5,2,14],[7,14,12,3],[11,12,5,11],[4,11,10,5],[2,15,14,2],[8,1,7,12]]

sbox4 = [[7,13,10,3],[13,8,6,15],[14,11,9,0],[3,5,0,6],[0,6,12,10],[6,15,11,1],[9,0,7,13],[10,3,13,8],[1,4,15,9],[2,7,1,4], \
    [8,2,3,5],[5,12,14,11],[11,1,5,12],[12,10,2,7],[4,14,8,2],[15,9,4,14]]

sbox5 = [[2,14,4,11],[12,11,2,8],[4,2,1,12],[1,12,11,7],[7,4,10,1],[10,7,13,14],[11,13,7,2],[6,1,8,13],[8,5,15,6],[5,0,9,15],\
    [3,15,12,0],[15,10,5,9],[13,3,6,10],[0,9,3,4],[14,8,0,5],[9,6,14,3]]

sbox6 = [[12,10,9,4],[1,15,14,3],[10,4,15,2],[15,2,5,12],[9,7,2,9],[2,12,8,5],[6,9,12,15],[8,5,3,10],[0,6,7,11],[13,1,0,14], \
    [3,13,4,1],[4,14,10,7],[14,0,1,6],[7,11,13,0],[5,3,11,8],[11,8,6,13]]

sbox7 = [[4,13,1,6],[11,0,4,11],[2,11,11,13],[14,7,13,8],[15,4,12,1],[0,9,3,4],[8,1,7,10],[13,10,14,7],[3,14,10,9],[12,3,15,5], \
    [9,5,6,0],[7,12,8,15],[5,2,0,14],[10,15,5,2],[6,8,9,3],[1,6,2,12]]

sbox8 = [[13,1,7,2],[2,15,11,1],[8,13,4,14],[4,8,1,7],[6,10,9,4],[15,3,12,10],[11,7,14,8],[1,4,2,13],[10,12,0,15],[9,5,6,12], \
    [3,6,10,9],[14,11,13,0],[5,0,15,3],[0,14,3,5],[12,9,5,6],[7,2,8,11]]

sboxs =[sbox1,sbox2,sbox3,sbox4,sbox5,sbox6,sbox7,sbox8]


# 儲存input
input = sys.argv[2] 
key = sys.argv[4]

# 將0x消除
input = input[2:]
key = key[2:]

# 長度太短補0
if(len(input)<4):
    for i in range(len(input), 16):
        input = '0' + input

if(len(key)<4):
    for i in range(len(key), 16):
        key = '0' + key

# handle inputs
input = bin(int(input, 16))[2:].zfill(64)
key = bin(int(key, 16))[2:].zfill(64)
input = string2list(input)
key = string2list(key)


first = [None] * 64

firstPermutation(first,input)

pc1 = [None] * 56
PC1(pc1,key)

left = first[:32]
right = first[32:]

c = pc1[:28]
d = pc1[28:]

pc2 = [None] * 48
exp = [None] * 48
xor = [None] * 48
sboxed = [None] * 32
lrxor = [None] * 32

for round in range(0,16):
    
    #############################處理subkey#########################
    if (round == 0 or round == 1 or round == 8 or round == 15):
        c = rotate(c, 1)
        d = rotate(d, 1)
    else:
        c = rotate(c, 2)
        d = rotate(d, 2)

    temp = c + d
    PC2(pc2, temp)
    ################################################################


    Expansion(exp,right)

    XOR(xor, exp, pc2, 48)

    # s-box substution
    for i in range(0,8):
        temp = xor[i * 6:(i + 1) * 6]
        num4 = temp[1] + temp[2] + temp[3] + temp[4]
        num4 = int(num4, 2)
        num2 = temp[0] + temp[5]
        num2 = int(num2 ,2)
        binary = sboxs[i][num4][num2]
        temp = format(binary, 'b').zfill(4)
        sboxed[i * 4:(i + 1) * 4] = temp

    copy = sboxed.copy()
    Permutation(sboxed, copy)

    temp = left.copy()
    left = right.copy()
    XOR(right,sboxed,temp,32)

left , right = right, left
ciphertext = left + right
temp = ciphertext.copy()
finalPermutation(ciphertext,temp)

# 轉換成hex
temp = ''
output = ''
for i in range(0, 16):
    hex_text = ciphertext[0 + 4 * i] + ciphertext[1 + 4 * i] + ciphertext[2 + 4 * i] + ciphertext[3 + 4 * i]
    hex_num = int(hex_text, 2)
    temp = hex(hex_num)
    output = output + temp[2]
output = output.upper()
output = '0x' + output 
print(output)
    






