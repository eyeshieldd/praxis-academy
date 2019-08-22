print('{0:.3f}'.format(1.0/3))

age = 25
name = 'johan'
print('umur saya', age )

c ='johan'
print(c[2:5])

masuk = int(input('jam masuk : '))
keluar = int(input('jam keluar : '))


lama = keluar - masuk
if lama <=2:
	biaya=lama*2000
else:
	biaya=lama*(2000+500)
print('lama parkir:',lama)
print('biaya parkir yang dibayarkan adalah :',biaya) 



