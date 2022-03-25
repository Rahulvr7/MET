import base64
import numpy as np
import random
def split(word):
    return [char for char in word]
def met(x):
    switcher={
        'a':2,
        'b':1,
        'c':10,
        'd':16,
        'e':3,
        'f':4,
        'g':12,
        'h':17,
        'i':5,
        'j':6,
        'k':13,
        'l':18,
        'm':21,
        'n':24,
        'o':7,
        'p':8,
        'q':14,
        'r':19,
        's':22,
        't':25,
        'u':11,
        'v':9,
        'w':15,
        'x':20,
        'y':23,
        'z':26,
        'A':2,
        'B':1,
        'C':10,
        'D':16,
        'E':3,
        'F':4,
        'G':12,
        'H':17,
        'I':5,
        'J':6,
        'K':13,
        'L':18,
        'M':21,
        'N':24,
        'O':7,
        'P':8,
        'Q':14,
        'R':19,
        'S':22,
        'T':25,
        'U':11,
        'V':9,
        'W':15,
        'X':20,
        'Y':23,
        'Z':26,
        '0':0,
        '1':1,
        '2':2,
        '3':3,
        '4':4,
        '5':5,
        '6':6,
        '7':7,
        '8':8,
        '9':9
        }
    return switcher.get(x)
print("\t\t\t\t\t\t\t\t\tSIMPLE MATRIX ENCRYPTION TECHNIQUE")
print("\nENCRYPTION:\n")
plain_txt = input("Enter text to be encrypted:")
plain_txt_bytes = plain_txt.encode("ascii")

base64_bytes = base64.b64encode(plain_txt_bytes)
base64_string = base64_bytes.decode("ascii")

print(f"\nEncoded string: {base64_string}\n")

l= len(base64_string)
c=base64_string.count("=")
l=l-c
code=base64_string[0:l]
s=(l%3)+2
substrings = [code[i:i+s] for i in range(0, l, s)]
#print(substrings)
nlist=[code[i:i+s] for i in range(0,l,s)]

for x in range(len(substrings)):
    substrings[x]=split(substrings[x])

for x in range(len(nlist)):
    nlist[x]=split(nlist[x])

for i in range(len(substrings)):
    for j in range(len(substrings[i])):
        substrings[i][j]=met(substrings[i][j])

#print(substrings)

while len(substrings[len(substrings)-1])!=len(substrings[len(substrings)-2]):
    substrings[len(substrings)-1].append(1)
m=len(substrings)%s
t=s-m
if s==2:
    while t!=0:
        substrings.append([1,1])
        t-=1
        
elif s==3:
    while t!=0:
        substrings.append([1,1,1])
        t-=1

elif s==4:
    while t!=0:
        substrings.append([1,1,1,1])
        t-=1
           

#print(substrings)

detm=[]
if s==2:
    for i in range(0,len(substrings),s):
        arr2=np.array([substrings[i],substrings[i+1]])
        #print(arr)
        D = np.linalg.det(arr2)
        detm.append(round(D%26))
    print("Determinants:",detm)

elif s==3:
    for i in range(0,len(substrings),s):
        arr3=np.array([substrings[i],substrings[i+1],substrings[i+2]])
        #print(arr)
        D = np.linalg.det(arr3)
        detm.append(round(D%26))
    print("Determinants:",detm)

elif s==4:
    for i in range(0,len(substrings),s):
        arr4=np.array([substrings[i],substrings[i+1],substrings[i+2],substrings[i+3]])
        #print(arr)
        D = np.linalg.det(arr4)
        detm.append(round(D%26))
    print("Determinants:",detm)
r=random.randint(1,99)
print("\nSecret key:",r)
for i in range(len(detm)):
    if len(detm)%2==0 :
        res = [x + r*i for x in detm]
    else:
        res = [x - r*i for x in detm]
print("\nEncrypted determinants:" + str(res))
#print(nlist)
k=0
cnt=0
f1=[]

for i in range(len(nlist)):
    for j in range(len(nlist[i])):
        if ord(nlist[i][j])>=65 and ord(nlist[i][j])<=90:
            d=ord(nlist[i][j])
            x=d-64
            #print(x)
            A=x+detm[k]
            if A>26:
                A-=26
            A=chr(A+64)
            #nlist[i][j]=A
            f1.append(A)
            
        elif ord(nlist[i][j])>=97 and ord(nlist[i][j])<=122:
            l=ord(nlist[i][j])
            p=l-96
            #print(p)
            b=p-detm[k]
            if b<=0:
                b+=26
            b=chr(b+96)
            #nlist[i][j]=a
            f1.append(b)
            
        elif ord(nlist[i][j])>=48 and ord(nlist[i][j])<=57:
            m=ord(nlist[i][j])
            n=m-48
            #print(n)
            #nlist[i][j]=m
            if n%2==0:
                n+=4
                if n>9:
                    n-=10
            else:
                n-=4
                if n<0:
                    n+=10
        
            f1.append(str(n))
            
        cnt+=1
   
    if cnt==(s*s):
        k+=1
        cnt=0
        
#print(f1)                               
ct=""
ct=ct.join(f1)
#print(ct)

print("\nENCRYPTED CODE:",ct,",",str(res))

#DECRYPTION
for i in range(len(res)):
    if len(res)%2==0 :
        dd = [x - r*i for x in res]
    else:
        dd = [x + r*i for x in res]
print("\n\nDECRYPTION:\n")
print("Decrypted determinants:" + str(dd))

f=(len(ct)%3)+2
dstr = [ct[i:i+s] for i in range(0,len(ct),f)]
#print(dstr)
for x in range(len(dstr)):
    dstr[x]=split(dstr[x])
#print(dstr)



dk=0
dcnt=0
df1=[]

for i in range(len(dstr)):
    for j in range(len(dstr[i])):
        if ord(dstr[i][j])>=65 and ord(dstr[i][j])<=90:
            d=ord(dstr[i][j])
            x=d-64
            #print(x)
            A=x-dd[dk]
            if A<=0:
                A+=26
            A=chr(A+64)
            #nlist[i][j]=A
            df1.append(A)
            
        elif ord(dstr[i][j])>=97 and ord(dstr[i][j])<=122:
            l=ord(dstr[i][j])
            p=l-96
            #print(p)
            b=p+dd[dk]
            if b>26:
                b-=26
            b=chr(b+96)
            #nlist[i][j]=a
            df1.append(b)
            
        elif ord(dstr[i][j])>=48 and ord(dstr[i][j])<=57:
            m=ord(dstr[i][j])
            n=m-48
            #print(n)
            #nlist[i][j]=m
            if n%2==0:
                n-=4
                if n<0:
                    n+=10
            else:
                n+=4
                if n>9:
                    n-=10
        
            df1.append(str(n))
            
        dcnt+=1
   
    if dcnt==(s*s):
        dk+=1
        dcnt=0
        
#print(df1)
dt=""
dt=dt.join(df1)
while c!=0:
    dt=dt + "="
    c-=1
print("\nDECRYPTED CODE:",dt)

dbase64_bytes = dt.encode("ascii")

dstring_bytes = base64.b64decode(dbase64_bytes)
dstring = dstring_bytes.decode("ascii")

print(f"\nDECRYPTED MESSAGE: {dstring}")


