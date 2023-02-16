# #Keyboar
# N = int(input('N = '))
# kiemtra = True
# #TH1: N<2
# if N<2:
#     kiemtra = False
# #TH2: N chia het cho so khac
# #Phan nguyen can bac 2 cua N : int(N**0.5)
# for i in range(2,int(N**0.5)+1):
#     if N % i == 0:
#         kiemtra = False
# if kiemtra:
#     print(f'{N} la so nguyen to')
# else:
#     print(f'{N} khong la so nguyen to')
#File
fi = open('prime.inp')
fo = open('prime.out','w')
N = int(fi.read())
kiemtra = True
#TH1: N<2
if N<2:
    kiemtra = False
#TH2: N chia het cho so khac
#Phan nguyen can bac 2 cua N : int(N**0.5)
for i in range(2,int(N**0.5)+1):
    if N % i == 0:
        kiemtra = False
if kiemtra:
    fo.write(f'{N} la so nguyen to')
else:
    fo.write(f'{N} khong la so nguyen to')

