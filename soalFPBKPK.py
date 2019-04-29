angka1=int(input('Masukkan angka pertama: '))
angka2=int(input('Masukkan angka kedua: '))

# FPB
i=1
j=1
faktor1=[]
faktor2=[]
while i<=angka1:
    if angka1%i==0:
        faktor1.append(i)
        i+=1
        if i>angka1:
            break
    elif angka1%i!=0:
        i+=1
        if i>angka1:
            break
print(faktor1)
while j<=angka2:
    if angka2%j==0:
        faktor2.append(j)
        j+=1
        if j>angka2:
            break
    elif angka2%j!=0:
        j+=1
        if j>angka2:
            break
print(faktor2)
k=0
faktorsekutu=[]
for l in faktor1:
    for k in faktor2:
        if l==k:
            faktorsekutu.append(l)
faktorsekutu.sort()
print('FPB-nya =',faktorsekutu[-1])

# KPK
i=2
j=2
kelipatan=[]
if angka1>angka2:
    if angka1%angka2==0:
        kelipatan.append(angka1)
    elif angka1%angka2!=0:
        while i>0:
            if angka2*i==angka1*j:
                kelipatan.append(angka2*i)
                break
            if angka2*i<angka1*j:
                i+=1
            if angka2*i>angka1*j:
                i=1
                j+=1
elif angka1<angka2:
    cek=angka1
    angka1=angka2
    angka2=cek
    if angka1%angka2==0:
        kelipatan.append(angka1)
    elif angka1%angka2!=0:
        while i>0:
            if angka2*i==angka1*j:
                kelipatan.append(angka2*i)
                break
            if angka2*i<angka1*j:
                i+=1
            if angka2*i>angka1*j:
                i=1
                j+=1
print('KPK-nya=',kelipatan[0])