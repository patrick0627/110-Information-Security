from pickle import FALSE
import sys, base64, random

# square and multiply
def square_and_multiply(num,mod,exp):

    exp = format(exp,'b')
    exp = str(exp)
    remainder= num % mod
    atom = num % mod
    index = 1

    while(index < len(exp)):
        if(exp[index] == '0'): #square
            remainder = (remainder * remainder) % mod
            index += 1
        else: #square and multiply
            remainder = (remainder * remainder) % mod
            remainder = (remainder * atom) % mod
            index += 1

    
    return remainder

# 加密
def encrypt(plaintext,n,e):


    e = int(e) 
    n = int(n)

    asc = ord(plaintext)
    remainder = square_and_multiply(asc,n,e)

    # 使出來結果長度一致 (長度330的string)
    result = str(remainder)
    for i in range(len(str(remainder)),330):
        result = "0" + result

    return result   

# 解密  
def decrypt(ciphertext,n,d):

    d = int(d)
    n = int(n)

    num = int(ciphertext)
    
    remainder= square_and_multiply(num,n,d)

    return chr(remainder)

# miller rabin test
def miller_rabin_test(num):
    # 取10次結果
    round = 10

    tmp = num -1
    k = 0
    while(int(tmp%2) == 0):
        k += 1
        tmp //= 2
    m = tmp

    for i in range(0,round):
        a = random.randint(2,num - 1)
        b = square_and_multiply(a,num,m)
       
        if(b == 1 or b == num - 1):
            continue
        for j in range(0,k-1):
            b = square_and_multiply(b,num,2)
            if(b == num - 1):
                break
        else:
            return False
    return True

# 找最大公因數
def gcd(x,y):
    if(y == 0):
        return x
    else:
        return gcd(y,x%y)

# 找到乘法反元素
def findInverse(a,m):
    if(gcd(a,m) != 1):
        return None
    u1,u2,u3 = 1,0,a
    v1,v2,v3 = 0,1,m
    while v3!=0:
        q = u3//v3
        v1,v2,v3,u1,u2,u3 = (u1-q*v1),(u2-q*v2),(u3-q*v3),v1,v2,v3
    return u1%m

# CRT算decrypt
def crt(result_p,result_q,p,q):
    count = 1
    while(True):
        
        if(result_q - result_p < 0):
            if((count * p) % q == q + result_q - result_p):
                return p * count + result_p
        else:
            if((count * p) % q == result_q - result_p):
                return p * count + result_p
        count += 1




if(sys.argv[1]  =="-i"):

    flag= False

    # 先取 p q
    while(not flag):

        p = random.randint(2**511+2**510,2**512-1)
        if(int(p % 2) == 0):
            continue
        flag = miller_rabin_test(p)

    
    flag = False
 
    while(not flag):

        q = random.randint(2**511+2**510,2**512-1)
        if(int(q % 2) == 0):
            continue
        flag = miller_rabin_test(q)


    n = p * q
    phi = (p-1) * (q-1)
    e = 1

    # 取e
    while(True):
        e = random.randint(1,phi-1)
        if(gcd(e,phi) == 1):
            break


    d = findInverse(e,phi)

    print("p = ", p)
    print("q = ", q)
    print("N = ", n)
    print("phi=", phi)
    print("e = ", e)
    print("d = ", d)

elif(sys.argv[1] == "-e"):

    msg = sys.argv[2]
    n = sys.argv[3]
    e = sys.argv[4]

    ciphertext= ""

    # 逐字加密
    for i in range(0,len(msg)):
        ciphertext = ciphertext + encrypt(msg[i],n,e)


    # 將結果轉成 base64
    ciphertext_uf8 = ciphertext.encode('UTF-8')
    result = base64.b64encode(ciphertext_uf8)
 
    print(result.decode('UTF-8'))
    
elif(sys.argv[1] == "-d"):

    ciphertext = sys.argv[2]
    n = sys.argv[3]
    d = sys.argv[4]

    # 要decrypt次數(一個字為長度440base64 因為330/3*4 = 440)
    round = int(len(ciphertext) / 440)


    ciphertext = base64.b64decode(ciphertext).decode('UTF-8') #先將 base64 decode

    plaintext = ""
    
    # 逐字解密
    for i in range(0,round):
        plaintext = plaintext + decrypt(ciphertext[i*330:330+i*330],n,d)
    
    print(plaintext)

elif(sys.argv[1] == "-CRT"):


    ciphertext = sys.argv[2]
    p = sys.argv[3]
    q = sys.argv[4]
    d = sys.argv[5]

    p = int(p)
    q = int(q)
    d = int(d)

    # ciphertext以440為一單位(因為330/3*4 = 440)
    round = int(len(ciphertext) / 440)

    ciphertext = base64.b64decode(ciphertext).decode('UTF-8') #先將 base64 decode

    plaintext = ""
    
    for i in range(0,round):

        simply_p = int(ciphertext[i*330:330+i*330]) % p 
        simply_exp = d % (p - 1) 
        result_p = square_and_multiply(int(simply_p),p,simply_exp)

        simply_q = int(ciphertext[i*330:330+i*330]) % q
        simply_exp = d % (q -1)
        result_q = square_and_multiply(int(simply_q),q,simply_exp)

        if(result_p == result_q):
            plaintext = plaintext + chr(result_p)
        else:
            result = crt(result_p,result_q,p,q)
            plaintext = plaintext + chr(result)

    print(plaintext)

else:
    print("wrong mode!")